"""
    This file contains Pydantic models for the FatAPI APP
"""

from pydantic import BaseModel
from typing import List




# Model the create blog (request) from the pydantic basemodel
class BlogBase(BaseModel):
    title: str
    body: str | None = None


class Blog(BlogBase):
    class Config():   
        orm_mode = True
        

# Request model for creating a user
class User(BaseModel):
    name: str
    email: str
    password: str
    
    
# Create the User Response Model
class ShowUser(BaseModel):
    name: str
    email: str
    # A user can have multiple blogs
    blogs: List[Blog] = []
    class Config():   
        orm_mode = True
        
        
# Response Model for showing blog as response
class ShowBlog(BaseModel):
    # The content to display in the response body
    title: str
    body: str 
    creator: ShowUser
    class Config():
        orm_mode = True

# This is the request from the login
class Login(BaseModel):
    username: str
    password: str
    

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None