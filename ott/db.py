from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:sri123@localhost:5432/ott"

# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:<password>@localhost:5432/ott"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 

Base = declarative_base()
