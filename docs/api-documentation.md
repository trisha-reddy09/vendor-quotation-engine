# API Documentation

## Vendor Endpoints

| Method | Path | Purpose |
|---|---|---|
| GET | `/vendors/` | List vendors |
| GET | `/vendors/{vendor_id}` | Get vendor |
| POST | `/vendors/` | Create vendor |
| PUT | `/vendors/{vendor_id}` | Update vendor |
| DELETE | `/vendors/{vendor_id}` | Delete vendor |

## Vendor Validation

| Field | Rule |
|---|---|
| vendor_name | Required, 2-120 characters, unique |
| contact_email | Valid email |
| phone | 7-20 characters |
| gst_number | Exactly 15 characters |

## Quote Endpoints

| Method | Path | Purpose |
|---|---|---|
| GET | `/quotes/` | List quotes |
| GET | `/quotes/{quote_id}` | Get quote |
| POST | `/quotes/` | Create quote |
| PUT | `/quotes/{quote_id}` | Update quote |
| DELETE | `/quotes/{quote_id}` | Delete quote |