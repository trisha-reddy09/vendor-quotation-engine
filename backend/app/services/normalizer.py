"""Turn messy vendor-supplied values into clean database values.

Every function:
- accepts whatever the vendor sent
- returns a clean value, or None when unusable
- never raises on ordinary messy input
"""

import re
from datetime import date, datetime
from decimal import Decimal, InvalidOperation
from typing import Optional


# -------------------------
# Amount
# -------------------------

CURRENCY_NOISE = re.compile(
    r"(rs\.?|inr|₹|/-|,|\s)",
    re.IGNORECASE
)


def normalize_amount(value) -> Optional[Decimal]:
    if value is None:
        return None

    if isinstance(value, (int, float, Decimal)):
        return Decimal(str(value))

    cleaned = CURRENCY_NOISE.sub("", str(value))

    if not cleaned:
        return None

    try:
        amount = Decimal(cleaned)
    except InvalidOperation:
        return None

    return amount if amount > 0 else None


# -------------------------
# Days
# -------------------------

WORD_NUMBERS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
}


def normalize_days(value) -> Optional[int]:
    if value is None:
        return None

    if isinstance(value, int):
        return value if value >= 0 else None

    text_value = str(value).strip().lower()

    if not text_value:
        return None

    match = re.search(r"(\d+(?:\.\d+)?)", text_value)

    if match:
        quantity = float(match.group(1))
    else:
        word = next(
            (w for w in WORD_NUMBERS if w in text_value),
            None
        )

        if word is None:
            return None

        quantity = WORD_NUMBERS[word]

    if "month" in text_value:
        multiplier = 30
    elif "week" in text_value:
        multiplier = 7
    else:
        multiplier = 1

    return int(round(quantity * multiplier))


# -------------------------
# Payment Terms
# -------------------------

def normalize_payment_terms(value) -> Optional[str]:
    if value is None:
        return None

    text_value = " ".join(str(value).split())

    if not text_value:
        return None

    lowered = text_value.lower()

    net_match = re.search(r"net\s*(\d+)", lowered)

    if net_match:
        return f"NET {net_match.group(1)}"

    if "advance" in lowered:
        return text_value.upper()

    if lowered in {
        "immediate",
        "immediately",
        "on delivery",
        "cod",
    }:
        return "IMMEDIATE"

    return text_value


def payment_terms_to_days(value) -> Optional[int]:
    cleaned = normalize_payment_terms(value)

    if cleaned is None:
        return None

    if cleaned == "IMMEDIATE":
        return 0

    match = re.search(
        r"net\s*(\d+)",
        cleaned,
        re.IGNORECASE
    )

    return int(match.group(1)) if match else None


# -------------------------
# Date
# -------------------------

DATE_FORMATS = [
    "%Y-%m-%d",
    "%d-%m-%Y",
    "%d/%m/%Y",
    "%Y/%m/%d",
    "%d.%m.%Y",
    "%B %d, %Y",
    "%d %B %Y",
    "%b %d, %Y",
]


def normalize_date(value) -> Optional[date]:
    if value is None:
        return None

    if isinstance(value, date):
        return value

    text_value = str(value).strip()

    if not text_value:
        return None

    for fmt in DATE_FORMATS:
        try:
            return datetime.strptime(text_value, fmt).date()
        except ValueError:
            continue

    return None


# -------------------------
# Quote Number
# -------------------------

def normalize_quote_number(value) -> Optional[str]:
    if value is None:
        return None

    cleaned = " ".join(str(value).split()).upper()

    cleaned = cleaned.replace("/", "-").replace("_", "-")

    cleaned = re.sub(r"-{2,}", "-", cleaned)

    return cleaned or None