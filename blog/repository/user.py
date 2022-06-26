"""
    This program implements the CRUD Operations on Users
"""
from typing import List
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

# Importing this from the main package
from database import get_db
from hashing import HashPassword
from models import UserTable
from schemas import ShowUser, User


#  Create a new user
def create(request: User, db : Session):
    # Hash the Password
    hashed_password = HashPassword(request.password)
    # Create the user 
    new_user = UserTable(name=request.name, email=request.email, password=hashed_password.get_hashed_password())
    # Add the new user
    db.add(new_user)
    # Commit the transaction
    db.commit()
    # Refresh on User
    db.refresh(new_user)
    return new_user


def read(id: int, db : Session):
    user = db.query(UserTable).filter(UserTable.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User with id {id} not found")
    return user


