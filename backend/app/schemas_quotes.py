from datetime import date, datetime
from decimal import Decimal
from typing import Optional
 
from pydantic import BaseModel
 
 
class QuoteBase(BaseModel):
    """Fields that describe a quotation, without database-generated values."""
    vendor_id: int
    quote_number: str
    quote_date: Optional[date] = None
    total_amount: Optional[Decimal] = None
    payment_terms: Optional[str] = None
    lead_time_days: Optional[int] = None
    validity_days: Optional[int] = None
 
 
class QuoteOut(QuoteBase):
    """What the API sends back to the client."""
    id: int
    created_at: Optional[datetime] = None
 
    class Config:
        from_attributes = True
 
 
class QuoteWithVendor(QuoteOut):
    """A quotation together with the name of the vendor who sent it."""
    vendor_name: Optional[str] = None
