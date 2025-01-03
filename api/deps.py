from sqlalchemy.orm import Session
from app.db.session import get_db
from fastapi import Depends

def get_database_session() -> Session:
    db = get_db()
    try:
        yield db
    finally:
        db.close()