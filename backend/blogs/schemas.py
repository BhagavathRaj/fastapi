# schemas.py
from pydantic import BaseModel

class Blog(BaseModel):  # Ensure the class is named 'Blog' (not 'BLog')
    title: str
    content: str
    author: str

class User(BaseModel):
    name: str
    email: str
    password: str
