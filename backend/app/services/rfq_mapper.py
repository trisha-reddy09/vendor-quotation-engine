"""Turn a raw RFQ file into a dictionary shaped like a quotes row.
 
This module saves nothing to the database. It reads (via rfq_reader),
cleans (via normalizer), and reports what it found - including what it
could not understand, so a human can review before importing.
"""
 
from typing import Any, Dict
 
from app.services.rfq_reader import load_rfq_file
from app.services.normalizer import (
    normalize_amount,
    normalize_date,
    normalize_days,
    normalize_payment_terms,
    normalize_quote_number,
)
 
 
def map_rfq(filename: str) -> Dict[str, Any]:
    """Read one RFQ file and map it to quote fields.
 
    Returns three things:
      quote    - the clean values, ready for the quotes table
      vendor   - the vendor details named in the file
      warnings - values that could not be understood
    """
    raw = load_rfq_file(filename)
 
    vendor_block = raw.get("vendor", {})
    quotation = raw.get("quotation", {})
 
    quote = {
        "quote_number": normalize_quote_number(quotation.get("quote_no")),
        "quote_date": normalize_date(quotation.get("quote_date")),
        "total_amount": normalize_amount(quotation.get("total")),
        "payment_terms": normalize_payment_terms(quotation.get("payment_terms")),
        "lead_time_days": normalize_days(quotation.get("lead_time")),
        "validity_days": normalize_days(quotation.get("validity")),
    }
 
    vendor = {
        "name": (vendor_block.get("name") or "").strip() or None,
        "email": vendor_block.get("email"),
        "gst": vendor_block.get("gst"),
    }
 
    warnings = _collect_warnings(quotation, quote, vendor)
 
    return {
        "source_file": filename,
        "vendor": vendor,
        "quote": quote,
        "warnings": warnings,
        "item_count": len(raw.get("items", [])),
    }
 
 
def _collect_warnings(quotation, quote, vendor):
    """Report every value the normalizer could not understand."""
    warnings = []
 
    checks = [
        ("quote_number", quotation.get("quote_no"), quote["quote_number"]),
        ("quote_date", quotation.get("quote_date"), quote["quote_date"]),
        ("total_amount", quotation.get("total"), quote["total_amount"]),
        ("lead_time_days", quotation.get("lead_time"), quote["lead_time_days"]),
        ("validity_days", quotation.get("validity"), quote["validity_days"]),
    ]
 
    for field, original, cleaned in checks:
        if original not in (None, "") and cleaned is None:
            warnings.append({
                "field": field,
                "original": original,
                "message": f"Could not understand {field}, will be saved as empty",
            })
 
    if not vendor["name"]:
        warnings.append({
            "field": "vendor_name",
            "original": None,
            "message": "The RFQ does not name a vendor",
        })
 
    if quote["quote_number"] is None:
        warnings.append({
            "field": "quote_number",
            "original": quotation.get("quote_no"),
            "message": "A quotation cannot be imported without a quote number",
        })
 
    return warnings
