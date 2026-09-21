# RFQ Normalization Rules

## 1. Amounts

Vendor prices may contain currency symbols, commas, spaces, or other formatting.

Examples:
- `Rs. 1,20,000/-` → `120000`
- `INR 95000.50` → `95000.50`
- `2,45,000` → `245000`

Invalid or empty values return `NULL`.

## 2. Lead Time and Validity

Time values are converted into days.

Rules:
- Days → same number
- Weeks → number × 7
- Months → number × 30

Examples:
- `10 working days` → `10`
- `2 weeks` → `14`
- `2 months` → `60`

## 3. Payment Terms

Payment terms are standardized where possible.

Examples:
- `Net 30 days` → `NET 30`
- `Immediate` → `IMMEDIATE`
- `COD` → `IMMEDIATE`
- Advance payment terms are converted to uppercase.

`payment_terms_to_days()` converts:
- `IMMEDIATE` → `0`
- `NET 30` → `30`

## 4. Dates

The normalizer accepts common date formats such as:

- `2026-03-15`
- `15-03-2026`
- `15/03/2026`
- `2026/03/15`
- `March 20, 2026`

Dates are stored in standard `YYYY-MM-DD` format.

## 5. Quote Numbers

Quote numbers are:
- converted to uppercase
- extra spaces removed
- `/` and `_` converted to `-`
- repeated hyphens reduced to one

Examples:
- `q-101` → `Q-101`
- `Q/103` → `Q-103`

## General Principle

The normalizer should not guess unknown values.

If a value cannot be understood safely, it returns `None` so that the original value can be reviewed manually.