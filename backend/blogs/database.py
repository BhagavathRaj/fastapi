from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL: Adjust this to your database type and credentials
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # Example for SQLite

# Create the engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Create the session local class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the base class for models
Base = declarative_base()
