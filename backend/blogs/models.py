# models.py
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()  # This defines the base class for your models

class Blog(Base):  # Inherit from Base
    __tablename__ = 'blogs'  # Define the table name
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)

    # You can add additional fields here as needed

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String)
    password = Column(String)