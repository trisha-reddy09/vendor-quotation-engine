from fastapi import APIRouter, HTTPException
from app.database import get_connection
from app.schemas import QuoteOut  # Use your actual quote schemas here

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