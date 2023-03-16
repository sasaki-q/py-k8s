import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db_config = {
    "host": os.getenv("DB_HOST", ""),
    "name": os.getenv("POSTGRES_DB", ""),
    "user": os.getenv("POSTGRES_USER", ""),
    "pass": os.getenv("DB_PASS", ""),
}

dns = f'postgresql://{db_config["user"]}:{db_config["pass"]}@{db_config["host"]}:5433/{db_config["name"]}'
Base = declarative_base()
engine = create_engine(dns, echo=True)

Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
