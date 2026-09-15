# Vendor API Design

## Overview

The Vendor API will manage vendor information for the Vendor Quotation Engine.

The API will support creating, viewing, updating, and deleting vendor records.

## Planned Endpoints

| Method | Endpoint | Purpose | Day 5 Status |
|--------|----------|---------|--------------|
| GET | /vendors | List all vendors | Design only |
| GET | /vendors/{id} | Get one vendor | Design only |
| POST | /vendors | Create a vendor | Design only |
| PUT | /vendors/{id} | Update a vendor | Design only |
| DELETE | /vendors/{id} | Delete a vendor | Design only |

## Vendor Data Fields

The Vendor API will use the following fields:

- id
- vendor_name
- contact_email
- phone
- address
- gst_number
- created_at

## Example POST Request

```json
{
  "vendor_name": "ABC Technologies",
  "contact_email": "abc@example.com",
  "phone": "9876543210",
  "address": "Bangalore",
  "gst_number": "29ABCDE1234F1Z5"
}