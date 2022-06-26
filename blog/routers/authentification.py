from database import get_db
from fastapi import APIRouter, Depends, status, HTTPException
from models import UserTable
from schemas import Login
from sqlalchemy.orm import Session
from hashing import UnHashPassword
from datetime import datetime, timedelta
from JWTtoken import create_access_token
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    tags=['authentication']
)


@router.post('/login', status_code=status.HTTP_200_OK)
def login(request : OAuth2PasswordRequestForm = Depends(), db : Session = Depends(get_db)):
    # Get the use via their email
    user = db.query(UserTable).filter(UserTable.email == request.username).first()
    # If not present in the db raise an exception
    if not user:
        raise HTTPException(status_code=404, detail=f"User with email {request.username} not found")
    
    # Compare the password
    password = UnHashPassword(request.password)
    if not password.verify_password(user.password):
        raise HTTPException(status_code=401, detail=f"Incorrect password")
    
    # Generate the token
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}