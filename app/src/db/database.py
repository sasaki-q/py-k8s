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


class RDSClientBase():
    Base = declarative_base()
    engine = create_engine(
        f'postgresql://{db_config["user"]}:{db_config["pass"]}@{db_config["host"]}:5433/{db_config["name"]}',
        echo=True
    )
    Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)

    def get_db(self):
        db = self.Session()
        try:
            yield db
        finally:
            db.close()
