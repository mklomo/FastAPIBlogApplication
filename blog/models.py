"""
    This file contains SQLAlchemy models
"""
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


# This model is connected to the db table
class BlogTable(Base):
    __tablename__ = 'blogs'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    
    # Foreign Key
    member_id = Column(Integer, ForeignKey("members.id"))
    creator = relationship("UserTable", back_populates='blogs')
    
    
class UserTable(Base):
    __tablename__ = 'members'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    
    blogs = relationship("BlogTable", back_populates='creator')
    
