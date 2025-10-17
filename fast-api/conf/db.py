from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
import os

SQLALCHEMY_DATABASE_USER = os.getenv("DATABASE_USER", "postgres")
SQLALCHEMY_DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", "567234")
SQLALCHEMY_DATABASE_HOST = os.getenv("DATABASE_HOST", "localhost")
SQLALCHEMY_DATABASE_NAME = os.getenv("DATABASE_NAME", "hw02")

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{SQLALCHEMY_DATABASE_USER}:{SQLALCHEMY_DATABASE_PASSWORD}@{SQLALCHEMY_DATABASE_HOST}:5432/{SQLALCHEMY_DATABASE_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True, max_overflow=5)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
