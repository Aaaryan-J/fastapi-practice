import time
from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, Query
import psycopg
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker
from psycopg.rows import dict_row
from .config import settings

SQLALCHEMY_DATABASE_URL = f'postgresql+psycopg://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()

while True:
    try:
        conn = psycopg.connect(
            host='localhost',
            dbname='fastapi_p',
            user='postgres',
            password='password',
            row_factory=dict_row,
        )
        cursor = conn.cursor()
        print("Database connection succesfull!")
        break
    except Exception as e:
        print(f"Database connection error: {e}")
        time.sleep(5)