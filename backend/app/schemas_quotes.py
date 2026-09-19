from datetime import date, datetime
from decimal import Decimal
from typing import Optional
 
from pydantic import BaseModel
from pydantic import Field, field_validator
 
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
      
class QuoteCreate(BaseModel):
    """What the client must send to create a quotation."""
    vendor_id: int = Field(..., gt=0, description="Must be an existing vendor id")
    quote_number: str = Field(..., min_length=1, max_length=50)
    quote_date: Optional[date] = None
    total_amount: Optional[Decimal] = Field(None, gt=0)
    payment_terms: Optional[str] = Field(None, max_length=100)
    lead_time_days: Optional[int] = Field(None, ge=0, le=365)
    validity_days: Optional[int] = Field(None, ge=0, le=365)
 
    @field_validator("quote_number")
    @classmethod
    def clean_quote_number(cls, value: str) -> str:
        cleaned = value.strip().upper()
        if not cleaned:
            raise ValueError("quote_number cannot be blank")
        return cleaned
 
 
class QuoteUpdate(BaseModel):
    """Every field optional - the client sends only what changes."""
    quote_number: Optional[str] = Field(None, min_length=1, max_length=50)
    quote_date: Optional[date] = None
    total_amount: Optional[Decimal] = Field(None, gt=0)
    payment_terms: Optional[str] = Field(None, max_length=100)
    lead_time_days: Optional[int] = Field(None, ge=0, le=365)
    validity_days: Optional[int] = Field(None, ge=0, le=365)
