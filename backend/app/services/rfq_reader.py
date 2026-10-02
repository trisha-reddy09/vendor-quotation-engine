"""Read mock RFQ files from disk.
 
This module does NOT touch the database and does NOT clean values.
Cleaning is normalizer.py's job; saving is Day 10's job.
"""
 
import json
from pathlib import Path
from typing import Any, Dict, List
 
# backend/app/services/rfq_reader.py -> up 3 levels -> project root
PROJECT_ROOT = Path(__file__).resolve().parents[3]
RFQ_DIR = PROJECT_ROOT / "data" / "mock_rfqs"
 
 
class RFQFileError(Exception):
    """Raised when an RFQ file is missing or unreadable."""
 
 
def list_rfq_files() -> List[str]:
    """Return the names of every RFQ file available."""
    if not RFQ_DIR.exists():
        return []
    return sorted(path.name for path in RFQ_DIR.glob("*.json"))
 
 
def load_rfq_file(filename: str) -> Dict[str, Any]:
    """Load one RFQ file by name and return its raw contents."""
    # Security: only allow a plain file name from our own folder.
    # Without this check, a request for "../../.env" could read secrets.
    if filename not in list_rfq_files():
        raise RFQFileError(f"RFQ file '{filename}' was not found")
 
    path = RFQ_DIR / filename
    try:
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except json.JSONDecodeError as exc:
        raise RFQFileError(f"RFQ file '{filename}' is not valid JSON: {exc}") from exc
 
 
def summarise_rfq(raw: Dict[str, Any]) -> Dict[str, Any]:
    """Pull out the fields we care about, still uncleaned."""
    vendor = raw.get("vendor", {})
    quotation = raw.get("quotation", {})
    return {
        "source_file": raw.get("source_file"),
        "vendor_name": vendor.get("name"),
        "vendor_email": vendor.get("email"),
        "raw_quote_number": quotation.get("quote_no"),
        "raw_quote_date": quotation.get("quote_date"),
        "raw_total": quotation.get("total"),
        "raw_payment_terms": quotation.get("payment_terms"),
        "raw_lead_time": quotation.get("lead_time"),
        "raw_validity": quotation.get("validity"),
        "item_count": len(raw.get("items", [])),
    }
