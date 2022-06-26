from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

# Importing this from the main package
from database import get_db
from hashing import HashPassword
from models import UserTable
from schemas import ShowUser, User
from repository import user


router = APIRouter(
    prefix='/user',
    tags=['user']
)




@router.post('/', status_code=status.HTTP_200_OK, response_model=ShowUser)
def create_user(request: User, db: Session = Depends(get_db)):
    return user.create(request=request, db=db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.read(id=id, db=db)
    