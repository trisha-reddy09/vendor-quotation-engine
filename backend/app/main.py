from fastapi import FastAPI
from app.routes.vendors import router as vendor_router
from app.routes import vendors, quotes


app = FastAPI(
    title="Vendor Quotation Engine API",
    version="0.1.0"
)


@app.get("/health")
def health_check():
    return {"status": "ok"}


app.include_router(vendor_router)

app.include_router(vendors.router)
app.include_router(quotes.router)   
