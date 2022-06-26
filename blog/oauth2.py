from smtplib import OLDSTYLE_AUTH
from fastapi import Depends, FastAPI, HTTPException, status
from JWTtoken import verify_token
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm




# Where will the token be fetched from? login route
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(token : str = Depends(oauth2_scheme)):
    return verify_token(token=token)
    
    
