from typing import Any, Dict, List
 
from fastapi import APIRouter
 
from app.errors import not_found, bad_request
from app.services.rfq_reader import (
    RFQFileError, list_rfq_files, load_rfq_file, summarise_rfq,
)
# add to the imports at the top
from sqlalchemy import text
from sqlalchemy.orm import Session
from fastapi import Depends, status
 
from app.database import get_db
from app.errors import conflict
from app.services.rfq_mapper import map_rfq
 

 
router = APIRouter(prefix="/rfq", tags=["RFQ"])
 
 
@router.get("/files", response_model=List[str])
def get_rfq_files():
    """List the mock RFQ files available to parse."""
    return list_rfq_files()
 
 
@router.get("/files/{filename}")
def get_rfq_file(filename: str) -> Dict[str, Any]:
    """Preview one RFQ file exactly as it is on disk. Nothing is saved."""
    try:
        raw = load_rfq_file(filename)
    except RFQFileError as exc:
        raise not_found("RFQ file", filename) from exc
    return raw
 
 
@router.get("/files/{filename}/summary")
def get_rfq_summary(filename: str) -> Dict[str, Any]:
    """Preview the fields we intend to map into the quotes table."""
    try:
        raw = load_rfq_file(filename)
    except RFQFileError as exc:
        raise not_found("RFQ file", filename) from exc
    return summarise_rfq(raw)


@router.get("/files/{filename}/mapped")
def get_rfq_mapped(filename: str) -> Dict[str, Any]:
    """Show what this RFQ would become. Nothing is saved."""
    try:
        return map_rfq(filename)
    except RFQFileError as exc:
        raise not_found("RFQ file", filename) from exc
    

@router.post("/files/{filename}/import", status_code=status.HTTP_201_CREATED)
def import_rfq(filename: str, db: Session = Depends(get_db)) -> Dict[str, Any]:
    """Import one RFQ file as a quotation for an existing vendor."""
    try:
        mapped = map_rfq(filename)
    except RFQFileError as exc:
        raise not_found("RFQ file", filename) from exc
 
    quote = mapped["quote"]
    vendor_name = mapped["vendor"]["name"]
 
    # 1. the file must name a vendor
    if not vendor_name:
        raise bad_request("This RFQ does not name a vendor, so it cannot be imported")
 
    # 2. a quotation must have a quote number
    if not quote["quote_number"]:
        raise bad_request("This RFQ has no readable quote number")
 
    # 3. the vendor must already exist (auto-create comes later)
    vendor_row = db.execute(
        text("SELECT id FROM vendors WHERE LOWER(vendor_name) = :name"),
        {"name": vendor_name.lower()},
    ).mappings().first()
 
    if vendor_row is None:
        raise not_found("Vendor", vendor_name)
 
    vendor_id = vendor_row["id"]
 
    # 4. the same quote number must not already exist for this vendor
    duplicate = db.execute(
        text(
            "SELECT id FROM quotes "
            "WHERE vendor_id = :vendor_id AND UPPER(quote_number) = :quote_number"
        ),
        {"vendor_id": vendor_id, "quote_number": quote["quote_number"]},
    ).first()
 
    if duplicate is not None:
        raise conflict(
            f"Quote {quote['quote_number']} already exists for {vendor_name}"
        )
 
    params = dict(quote)
    params["vendor_id"] = vendor_id
 
    row = db.execute(
        text(
            """
            INSERT INTO quotes (vendor_id, quote_number, quote_date, total_amount,
                                payment_terms, lead_time_days, validity_days)
            VALUES (:vendor_id, :quote_number, :quote_date, :total_amount,
                    :payment_terms, :lead_time_days, :validity_days)
            RETURNING id, vendor_id, quote_number, quote_date, total_amount,
                      payment_terms, lead_time_days, validity_days, created_at
            """
        ),
        params,
    ).mappings().first()
 
    db.commit()
 
    return {
        "imported": True,
        "source_file": filename,
        "quote": dict(row),
        "warnings": mapped["warnings"],
    }
