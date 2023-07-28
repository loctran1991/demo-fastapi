from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import urllib.parse #if your password has specific letter, you should use this lib
from app.config import settings


postgres_pwd = urllib.parse.quote_plus(settings.database_password)

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{settings.database_username}:{postgres_pwd}@{settings.database_hostname}/{settings.database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()