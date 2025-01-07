from fastapi import FastAPI
from schemas import Blog
# In main.py
import models
from database import engine
app=FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.post("/blog")
def create_blog(request: Blog):
    return request

@app.post("/create/blog")
def create_blog(request: Blog):
    return request
