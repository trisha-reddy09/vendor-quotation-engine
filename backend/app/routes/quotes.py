from fastapi import APIRouter, Depends, Query, status
from sqlalchemy import text
from sqlalchemy.orm import Session
from app.database import get_connection, get_db
from app.errors import not_found, conflict, bad_request
from app.schemas_quotes import QuoteOut, QuoteWithVendor, QuoteCreate, QuoteUpdate
 

router = APIRouter(
    prefix="/quotes",
    tags=["Quotes"]
)

@router.get("/")
def get_quotes():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT 
                    id,
                    vendor_id,
                    quote_number,
                    quote_date,
                    total_amount,
                    payment_terms,
                    lead_time_days,
                    validity_days
                FROM quotes
                ORDER BY id
            """)
            rows = cur.fetchall()
            
    return [
        {
            "id": row[0],
            "vendor_id": row[1],
            "quote_number": row[2],
            "quote_date": row[3],
            "total_amount": row[4],
            "payment_terms": row[5],
            "lead_time_days": row[6],
            "validity_days": row[7]
        }
        for row in rows
    ]
@router.get("/{quote_id}", response_model=QuoteOut)    
def get_quote(quote_id: int, db: Session = Depends(get_db)):
    """Get a single quotation by ID."""
    row = db.execute(
        text("""
            SELECT 
                id, vendor_id, quote_number, quote_date, total_amount,
                payment_terms, lead_time_days, validity_days
            FROM quotes
            WHERE id = :quote_id
        """),
        {"quote_id": quote_id}
    ).mappings().first()
    
    if row is None:
        raise not_found("Quote", quote_id)
        
    return row
    
# --- small helpers used by more than one endpoint ---
 
def _vendor_exists(db, vendor_id: int) -> bool:
    row = db.execute(
        text("SELECT 1 FROM vendors WHERE id = :vendor_id"),
        {"vendor_id": vendor_id},
    ).first()
    return row is not None
 
 
def _quote_number_taken(db, vendor_id: int, quote_number: str,
                        ignore_quote_id: int = None) -> bool:
    sql = ("SELECT 1 FROM quotes "
           "WHERE vendor_id = :vendor_id AND UPPER(quote_number) = :quote_number")
    params = {"vendor_id": vendor_id, "quote_number": quote_number.upper()}
    if ignore_quote_id is not None:
        sql += " AND id <> :ignore_id"
        params["ignore_id"] = ignore_quote_id
    return db.execute(text(sql), params).first() is not None
 
 
# --- CREATE ---
 
@router.post("/", response_model=QuoteOut, status_code=status.HTTP_201_CREATED)
def create_quote(payload: QuoteCreate, db: Session = Depends(get_db)):
    """Create a new quotation for an existing vendor."""
    if not _vendor_exists(db, payload.vendor_id):
        raise not_found("Vendor", payload.vendor_id)
 
    if _quote_number_taken(db, payload.vendor_id, payload.quote_number):
        raise conflict(
            f"Quote number {payload.quote_number} already exists "
            f"for vendor {payload.vendor_id}"
        )
 
    sql = text(
        """
        INSERT INTO quotes (vendor_id, quote_number, quote_date, total_amount,
                            payment_terms, lead_time_days, validity_days)
        VALUES (:vendor_id, :quote_number, :quote_date, :total_amount,
                :payment_terms, :lead_time_days, :validity_days)
        RETURNING id, vendor_id, quote_number, quote_date, total_amount,
                  payment_terms, lead_time_days, validity_days, created_at
        """
    )
    row = db.execute(sql, payload.model_dump()).mappings().first()
    db.commit()
    return row
 
 
# --- UPDATE ---
 
@router.put("/{quote_id}", response_model=QuoteOut)
def update_quote(quote_id: int, payload: QuoteUpdate,
                 db: Session = Depends(get_db)):
    """Update only the fields that were actually sent."""
    existing = db.execute(
        text("SELECT id, vendor_id FROM quotes WHERE id = :quote_id"),
        {"quote_id": quote_id},
    ).mappings().first()
 
    if existing is None:
        raise not_found("Quote", quote_id)
 
    changes = payload.model_dump(exclude_unset=True)
    if not changes:
        raise bad_request("No fields were provided to update")
 
    if "quote_number" in changes:
        changes["quote_number"] = changes["quote_number"].strip().upper()
        if _quote_number_taken(db, existing["vendor_id"],
                               changes["quote_number"], ignore_quote_id=quote_id):
            raise conflict(
                f"Quote number {changes['quote_number']} already exists "
                f"for this vendor"
            )
 
    set_clause = ", ".join(f"{field} = :{field}" for field in changes)
    params = dict(changes)
    params["quote_id"] = quote_id
 
    sql = text(
        f"""
        UPDATE quotes SET {set_clause}
        WHERE id = :quote_id
        RETURNING id, vendor_id, quote_number, quote_date, total_amount,
                  payment_terms, lead_time_days, validity_days, created_at
        """
    )
    row = db.execute(sql, params).mappings().first()
    db.commit()
    return row
 
 
# --- DELETE ---
 
@router.delete("/{quote_id}", status_code=status.HTTP_200_OK)
def delete_quote(quote_id: int, db: Session = Depends(get_db)):
    """Delete a quotation by id."""
    row = db.execute(
        text("DELETE FROM quotes WHERE id = :quote_id RETURNING id"),
        {"quote_id": quote_id},
    ).first()
 
    if row is None:
        raise not_found("Quote", quote_id)
 
    db.commit()
    return {"deleted": True, "id": quote_id}
    