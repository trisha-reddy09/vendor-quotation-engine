from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import VendorCreate
from app.errors import not_found, conflict


router = APIRouter(
    prefix="/vendors",
    tags=["Vendors"]
)


def _vendor_name_taken(
    db: Session,
    vendor_name: str,
    ignore_vendor_id: int = None
) -> bool:
    """
    Check whether a vendor with the same name already exists.
    The comparison is case-insensitive.
    """
    sql = "SELECT 1 FROM vendors WHERE LOWER(vendor_name) = :name"
    params = {"name": vendor_name.lower()}

    if ignore_vendor_id is not None:
        sql += " AND id <> :ignore_id"
        params["ignore_id"] = ignore_vendor_id

    result = db.execute(text(sql), params)
    return result.first() is not None


@router.get("/")
def get_vendors(db: Session = Depends(get_db)):
    rows = db.execute(
        text(
            """
            SELECT
                id,
                vendor_name,
                contact_email,
                phone,
                address,
                gst_number
            FROM vendors
            ORDER BY id
            """
        )
    ).mappings().all()

    return rows


@router.get("/{vendor_id}")
def get_vendor(
    vendor_id: int,
    db: Session = Depends(get_db)
):
    row = db.execute(
        text(
            """
            SELECT
                id,
                vendor_name,
                contact_email,
                phone,
                address,
                gst_number
            FROM vendors
            WHERE id = :vendor_id
            """
        ),
        {"vendor_id": vendor_id},
    ).mappings().first()

    if row is None:
        raise not_found("Vendor", vendor_id)

    return row


@router.post("/")
def create_vendor(
    vendor: VendorCreate,
    db: Session = Depends(get_db)
):
    # Check for duplicate vendor name
    if _vendor_name_taken(db, vendor.vendor_name):
        raise conflict(
            f"A vendor named '{vendor.vendor_name}' already exists"
        )

    row = db.execute(
        text(
            """
            INSERT INTO vendors
            (vendor_name, contact_email, phone, address, gst_number)
            VALUES
            (:vendor_name, :contact_email, :phone, :address, :gst_number)
            RETURNING
                id,
                vendor_name,
                contact_email,
                phone,
                address,
                gst_number
            """
        ),
        {
            "vendor_name": vendor.vendor_name,
            "contact_email": vendor.contact_email,
            "phone": vendor.phone,
            "address": vendor.address,
            "gst_number": vendor.gst_number,
        },
    ).mappings().first()

    db.commit()

    return row


@router.put("/{vendor_id}")
def update_vendor(
    vendor_id: int,
    vendor: VendorCreate,
    db: Session = Depends(get_db)
):
    # Check whether vendor exists
    existing = db.execute(
        text("SELECT id FROM vendors WHERE id = :vendor_id"),
        {"vendor_id": vendor_id},
    ).first()

    if existing is None:
        raise not_found("Vendor", vendor_id)

    # Check for duplicate vendor name
    if _vendor_name_taken(
        db,
        vendor.vendor_name,
        ignore_vendor_id=vendor_id
    ):
        raise conflict(
            f"A vendor named '{vendor.vendor_name}' already exists"
        )

    row = db.execute(
        text(
            """
            UPDATE vendors
            SET
                vendor_name = :vendor_name,
                contact_email = :contact_email,
                phone = :phone,
                address = :address,
                gst_number = :gst_number
            WHERE id = :vendor_id
            RETURNING
                id,
                vendor_name,
                contact_email,
                phone,
                address,
                gst_number
            """
        ),
        {
            "vendor_name": vendor.vendor_name,
            "contact_email": vendor.contact_email,
            "phone": vendor.phone,
            "address": vendor.address,
            "gst_number": vendor.gst_number,
            "vendor_id": vendor_id,
        },
    ).mappings().first()

    db.commit()

    return row


@router.delete("/{vendor_id}")
def delete_vendor(
    vendor_id: int,
    db: Session = Depends(get_db)
):
    existing = db.execute(
        text("SELECT id FROM vendors WHERE id = :vendor_id"),
        {"vendor_id": vendor_id},
    ).first()

    if existing is None:
        raise not_found("Vendor", vendor_id)

    deleted = db.execute(
        text(
            """
            DELETE FROM vendors
            WHERE id = :vendor_id
            RETURNING id
            """
        ),
        {"vendor_id": vendor_id},
    ).first()

    db.commit()

    return {
        "message": "Vendor deleted successfully",
        "id": deleted[0]
    }


def find_vendor_by_name(db: Session, vendor_name: str):
    """
    Return the vendor row matching this name, or None.
    Matching ignores case and extra spaces, because vendors write
    their own name differently on every document.
    """
    if not vendor_name:
        return None

    cleaned = " ".join(vendor_name.split()).lower()

    return db.execute(
        text(
            """
            SELECT id, vendor_name, contact_email
            FROM vendors
            WHERE LOWER(vendor_name) = :name
            """
        ),
        {"name": cleaned},
    ).mappings().first()


def create_vendor_from_rfq(
    db: Session,
    name: str,
    email: str = None,
    gst: str = None
):
    """
    Create a minimal vendor record from RFQ details.
    """
    row = db.execute(
        text(
            """
            INSERT INTO vendors
            (vendor_name, contact_email, gst_number)
            VALUES
            (:name, :email, :gst)
            RETURNING
                id,
                vendor_name,
                contact_email,
                gst_number,
                created_at
            """
        ),
        {
            "name": " ".join(name.split()),
            "email": email,
            "gst": gst,
        },
    ).mappings().first()

    db.commit()

    return row