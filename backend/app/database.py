import os
import psycopg


DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:YOUR_PASSWORD@localhost:5432/vendor_quotation_db"
)


def get_connection():
    return psycopg.connect(DATABASE_URL)