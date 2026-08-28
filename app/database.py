from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os


# Link do PostgreSQL
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("A variável DATABASE_URL não foi encontrada no arquivo .env")

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()





