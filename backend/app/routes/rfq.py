from typing import Any, Dict, List
 
from fastapi import APIRouter
 
from app.errors import not_found, bad_request
from app.services.rfq_reader import (
    RFQFileError, list_rfq_files, load_rfq_file, summarise_rfq,
)
 
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
