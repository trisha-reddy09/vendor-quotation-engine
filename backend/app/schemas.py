from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Optional
from datetime import date
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
    vendor_name: str = Field(..., min_length=2, max_length=120)
    contact_email: Optional[EmailStr] = None
    phone: Optional[str] = Field(None, min_length=7, max_length=20)
    address: Optional[str] = Field(None, max_length=300)
    gst_number: Optional[str] = Field(None, min_length=15, max_length=15)

    @field_validator("vendor_name")
    @classmethod
    def clean_name(cls, value: str) -> str:
        cleaned = " ".join(value.split())
        if not cleaned:
            raise ValueError("vendor_name cannot be blank")
        return cleaned

    @field_validator("gst_number")
    @classmethod
    def upper_gst(cls, value):
        return value.upper() if value else value


class VendorResponse(VendorCreate):
    id: int