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

## 7. RFQ endpoints (Days 16 and 17)

| Method | Path | Purpose |
|---|---|---|
| GET | `/rfq/files` | List available RFQ files |
| POST | `/rfq/files/{name}/import` | Import one RFQ file |
| POST | `/rfq/import-all` | Import all available RFQ files |

### Import behavior

The RFQ import endpoints support vendor matching and optional vendor creation.

| Case | Behavior |
|---|---|
| Vendor matches an existing vendor | RFQ is imported using the matched vendor |
| Vendor does not match and `create_vendor=false` | Import is refused |
| Vendor does not match and `create_vendor=true` | A new vendor can be created |
| Invalid or unsupported RFQ data | Import is refused with an appropriate error |

The `create_vendor` option is disabled by default.