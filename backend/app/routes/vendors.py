from fastapi import APIRouter
from app.database import get_connection
from fastapi import APIRouter, HTTPException
from app.schemas import VendorCreate

router = APIRouter(
    prefix="/vendors",
    tags=["Vendors"]
)


@router.get("/")
def get_vendors():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT
                    id,
                    vendor_name,
                    contact_email,
                    phone,
                    address,
                    gst_number
                FROM vendors
                ORDER BY id
            """)

            rows = cur.fetchall()

    return [
        {
            "id": row[0],
            "vendor_name": row[1],
            "contact_email": row[2],
            "phone": row[3],
            "address": row[4],
            "gst_number": row[5]
        }
        for row in rows
    ]
  
@router.get("/{vendor_id}")
def get_vendor(vendor_id: int):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT
                    id,
                    vendor_name,
                    contact_email,
                    phone,
                    address,
                    gst_number
                FROM vendors
                WHERE id = %s
            """, (vendor_id,))

            row = cur.fetchone()

    if row is None:
        raise HTTPException(
            status_code=404,
            detail="Vendor not found"
        )

    return {
        "id": row[0],
        "vendor_name": row[1],
        "contact_email": row[2],
        "phone": row[3],
        "address": row[4],
        "gst_number": row[5]
    }  


@router.post("/")
def create_vendor(vendor: VendorCreate):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO vendors
                (vendor_name, contact_email, phone, address, gst_number)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING
                    id,
                    vendor_name,
                    contact_email,
                    phone,
                    address,
                    gst_number
            """, (
                vendor.vendor_name,
                vendor.contact_email,
                vendor.phone,
                vendor.address,
                vendor.gst_number
            ))

            row = cur.fetchone()

        conn.commit()

    return {
        "id": row[0],
        "vendor_name": row[1],
        "contact_email": row[2],
        "phone": row[3],
        "address": row[4],
        "gst_number": row[5]
    }    


@router.put("/{vendor_id}")
def update_vendor(vendor_id: int, vendor: VendorCreate):
    with get_connection() as conn:
        with conn.cursor() as cur:

            cur.execute(
                "SELECT id FROM vendors WHERE id = %s",
                (vendor_id,)
            )

            existing = cur.fetchone()

            if existing is None:
                raise HTTPException(
                    status_code=404,
                    detail="Vendor not found"
                )

            cur.execute("""
                UPDATE vendors
                SET
                    vendor_name = %s,
                    contact_email = %s,
                    phone = %s,
                    address = %s,
                    gst_number = %s
                WHERE id = %s
                RETURNING
                    id,
                    vendor_name,
                    contact_email,
                    phone,
                    address,
                    gst_number
            """, (
                vendor.vendor_name,
                vendor.contact_email,
                vendor.phone,
                vendor.address,
                vendor.gst_number,
                vendor_id
            ))

            row = cur.fetchone()

        conn.commit()

    return {
        "id": row[0],
        "vendor_name": row[1],
        "contact_email": row[2],
        "phone": row[3],
        "address": row[4],
        "gst_number": row[5]
    }

@router.delete("/{vendor_id}")
def delete_vendor(vendor_id: int):
    with get_connection() as conn:
        with conn.cursor() as cur:

            cur.execute(
                "SELECT id FROM vendors WHERE id = %s",
                (vendor_id,)
            )

            existing = cur.fetchone()

            if existing is None:
                raise HTTPException(
                    status_code=404,
                    detail="Vendor not found"
                )

            cur.execute(
                "DELETE FROM vendors WHERE id = %s RETURNING id",
                (vendor_id,)
            )

            deleted_id = cur.fetchone()[0]

        conn.commit()

    return {
        "message": "Vendor deleted successfully",
        "id": deleted_id
    }        