from fastapi import FastAPI, Depends,status,Response,HTTPException,Request
from schemas import Blog 
import models ,schemas
from database import engine, SessionLocal 
from sqlalchemy.orm import Session

app = FastAPI()

# Create all database tables
models.Base.metadata.create_all(bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.post("/blog")
def create_blog(request: Blog):
    return request

@app.post("/create/blog",status_code=status.HTTP_201_CREATED)
def create_blog_entry(request: Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get("/blog/{id}",status_code=status.HTTP_201_CREATED)
def show (id,response:Response, db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with the id {id} is not available")
       
    return blogs

@app.delete("/blog/{id}",status_code=status.HTTP_204_NO_CONTENT)
def deleteBlod(id,db: Session = Depends(get_db)):
    blogs=db.query(models.Blog).filter(models.Blog.id==id).delete(synchronize_session=False)
    db.commit()
    return 'done'
@app.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with the id {id} is not available"
        )
    
    blog.title = request.title  # Assuming `title` is a field in your `schemas.Blog`
    blog.content = request.content  # Adjust fields as per your model
    
    db.commit()
    return {"detail": f"Blog with id {id} has been updated"}