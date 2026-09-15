from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime
from decimal import Decimal

class QuoteOut(BaseModel):
    id: int
    vendor_id: int
    quote_number: str
    quote_date: Optional[date] = None
    total_amount: Optional[Decimal] = None
    payment_terms: Optional[str] = None
    lead_time_days: Optional[int] = None
    validity_days: Optional[int] = None

    class Config:
        from_attributes = True


class VendorCreate(BaseModel):
    vendor_name: str
    contact_email: str | None = None
    phone: str | None = None
    address: str | None = None
    gst_number: str | None = None


class VendorResponse(VendorCreate):
    id: int
