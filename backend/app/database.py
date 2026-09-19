import os
from pathlib import Path
from dotenv import load_dotenv
import psycopg
from psycopg.rows import dict_row
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
ENV_PATH = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(ENV_PATH)




DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError(f"DATABASE_URL is not set - looked for {ENV_PATH}")


def get_connection():
    """Raw psycopg3 connection, used by the vendor and quote read code."""
    return psycopg.connect(
        DATABASE_URL.replace("+psycopg", ""),
        row_factory=dict_row,
    )


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    """FastAPI dependency for SQLAlchemy sessions."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()