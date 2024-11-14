from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import os
from dotenv import load_dotenv
from typing import Generator

load_dotenv()

DATABASE_URL: str = os.getenv("DATABASE_URL")

# Database engine configuration
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db() -> Generator[Session, None, None]:
    """
    Provides a database session for dependency injection in FastAPI routes.

    Yields:
        Generator[Session, None, None]: The database session instance.

    Closes:
        The session is closed after use to release database resources.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
