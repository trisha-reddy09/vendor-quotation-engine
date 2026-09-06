# Database Schema 
## vendors 
Stores vendor information. 
## quotes 
Stores quotations received from vendors. 
## Relationship 
One vendor can have many quotes. 
vendors.id -> quotes.vendor_id

## Day 4 – Database Verification

The PostgreSQL vendor and quote database was successfully verified.

- PostgreSQL connection was tested successfully.
- `schema.sql` was executed without errors.
- Vendor records were inserted successfully using `seed.sql`.
- Quote records were inserted successfully using `seed.sql`.
- Vendor and quote records were verified using `SELECT` queries.
- The relationship between vendors and quotes was verified using an SQL `JOIN`.
- Each quote is correctly associated with its corresponding vendor through `vendor_id`.