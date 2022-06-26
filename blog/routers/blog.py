from typing import List

# Importing this from the main package
from database import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from models import Base, BlogTable
from repository import blog
from schemas import Blog, ShowBlog, User
from sqlalchemy.orm import Session
from oauth2 import get_current_user

router = APIRouter(
    prefix='/blog',
    tags = ['blog']
)



#  Get All blogs from DB
@router.get('/',status_code=status.HTTP_200_OK, response_model=List[ShowBlog])
def get_blogs(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    # return all blogs
    return blog.get_all(db=db)


# Lets begin by creating a blog
@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: Blog, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return blog.create(request=request, db=db, created_by=current_user)



# Delete the blog
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id : int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return blog.delete(id=id, db=db)
    

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id : int, request: Blog, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return blog.update(id=id, request=request, db=db, updated_by=current_user)






@router.get('/blog/{id}', status_code=status.HTTP_200_OK, response_model=ShowBlog)
def get_specific_blog(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return blog.get_single(id=id, db=db)
