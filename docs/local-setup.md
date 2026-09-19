# Local Setup Guide
 
Written after the Day 16 environment problems. Follow this in order.
 
## 1. One virtual environment only
The project uses `venv` (no dot). If a `.venv` folder appears,
delete it - having both causes "No module named sqlalchemy" errors
even though the package is installed.
 
    venv\Scripts\activate          # prompt should read (venv)
 
## 2. Install dependencies
 
    python -m pip install -r backend/requirements.txt
 
## 3. PostgreSQL driver
This project uses psycopg3, not psycopg2. The DATABASE_URL must say
`postgresql+psycopg://` so SQLAlchemy loads the right driver.
 
## 4. Create your .env in the PROJECT ROOT (not in backend/)
 
    DATABASE_URL=postgresql+psycopg://postgres:YOUR_PASSWORD@localhost:5432/vendor_quotation_db
 
Check your real port in pgAdmin (Properties > Connection). It is
usually 5432. Never commit this file.
 
## 5. Confirm the password works before blaming the code
 
    psql -h localhost -p 5432 -U postgres -d vendor_quotation_db -c "SELECT count(*) FROM vendors;"
 
If psql works but the API says "password authentication failed",
the password in .env is wrong or has a stray space.
 
## 6. Run the server FROM the backend folder
 
    cd backend
    uvicorn app.main:app --reload
 
Running it from the project root fails with "No module named app".
 
## 7. Select the right interpreter in VS Code
Ctrl+Shift+P > Python: Select Interpreter > the one inside
vendor-quotation-engine\venv. If VS Code shows "Import could not be
resolved" warnings while the terminal runs fine, this is the cause.
 
## 8. Reading errors
Swagger only ever says "Internal Server Error". The real traceback is
in the uvicorn terminal - always read its LAST line first. To capture it:
 
    uvicorn app.main:app 2>&1 | Tee-Object -FilePath error.log
 
Start the server, make the failing request in Swagger, THEN stop the
server and read error.log. Stopping it first captures nothing.
