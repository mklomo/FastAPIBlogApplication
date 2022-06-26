"""
        This program implements CRUD Operation for the BLOG
"""
from fastapi import HTTPException, status
from models import BlogTable, UserTable
from database import Base
from schemas import Blog
from sqlalchemy.orm import Session


# Get All Blogs
def get_all(db: Session):
    blogs = db.query(BlogTable).all()
    return blogs


# Get Single Blog with ID
def get_single(db: Session, id: int):
    # Query the DB model for a specific blog
    blog = db.query(BlogTable).filter(BlogTable.id == id).first()
    if not blog:
        raise HTTPException(status_code=404, detail=f"Blog with id {id} not found")
    return blog


# Create a New Blog
def create(request : Blog, db: Session, created_by):
    # Get the member id of the current user
    creater_id = db.query(UserTable).filter(UserTable.email == created_by).first().id
    # Get the request Dictionary as a kwargs
    new_blog = BlogTable(**request.dict(), member_id=creater_id)
    # Add the new blog to the Database
    db.add(new_blog)
    # Commit to the DB
    db.commit()
    # refresh the newly created blog to return this blog
    db.refresh(new_blog)
    # Return the newly created blog
    return new_blog


# Update and existing blog by specifying an ID
def update(db : Session, request: Blog, id : int, updated_by):
    # Updated by the current user
    updater_id = db.query(UserTable).filter(UserTable.email == updated_by).first().id
    # Find the blog
    blog = db.query(BlogTable).filter(BlogTable.id == id)
    
    # Check if blog is empty
    if not blog.first():
        raise HTTPException(status_code=404, detail=f"Blog with {id} not found")
    
    else:
        update_dict = request.dict()
        update_dict['member_id'] = updater_id
        blog.update(update_dict)
        # Commit the Transaction
        db.commit()
        # Return the request
        return request.dict()
    

# Delete an Existing Blog
def delete(db : Session, id : int):
    # Delete the blog
    blog = db.query(BlogTable).filter(BlogTable.id == id)
    
    if not blog.first():
        raise HTTPException(status_code=404, detail=f"Blog with {id} not found")
    
    else:
        blog.delete(synchronize_session=False)  # type: ignore
        db.commit()
        # return
        return {f"Blog with id {id} has been deleted"}
    