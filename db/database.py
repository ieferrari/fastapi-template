from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os

try:
    from ..secrets import *
except ModuleNotFoundError:
    DB_USER = os.environ.get('DB_USER','')
    DB_PASS = os.environ.get('DB_PASS','')
    DB_HOST = os.environ.get('DB_HOST','')

SQLALCHEMY_DATABASE_URL = "postgresql://" + \
                          DB_USER + ":" + DB_PASS + "@" + DB_HOST + ":5432/iot"


# SQLALCHEMY_DATABASE_URL = "sqlite:///./app_database_connection/sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(SQLALCHEMY_DATABASE_URL,
                       # connect_args={"check_same_thread": False}
                       )
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# for sqlite also uncomment line 11
