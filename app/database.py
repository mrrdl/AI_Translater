import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy import sessionmaker

load_dotenv()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

SQLALCHEMY_DATABASE_URL=os.dotenv("DATABASE_URL")
engine=create_engine(SQLALCHEMY_DATABASE_URL)