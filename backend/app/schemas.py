from pydantic import BaseModel


class VendorCreate(BaseModel):
    vendor_name: str
    contact_email: str | None = None
    phone: str | None = None
    address: str | None = None
    gst_number: str | None = None


class VendorResponse(VendorCreate):
    id: int