from typing import List

from fastapi import Depends, FastAPI

# from blog.routers import blog
import routers.blog as blog
import routers.user as user
import routers.authentification as authentication
from database import engine
from models import Base

# Create the database tables for the blog
Base.metadata.create_all(bind=engine) 



# Create the database table for the user
# UserTable.metadata.create_all(bind=engine)


# Instantiate the App
app =  FastAPI()


# Include route for authentication
app.include_router(authentication.router)

# Include the router path for blog
app.include_router(blog.router)

# Include route for for user
app.include_router(user.router)


# # Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()



# # Lets begin by creating a blog
# @app.post('/blog', tags=['blogs'])
# def create(request: Blog, db: Session = Depends(get_db), status_code=status.HTTP_201_CREATED):
#     # Get the request Dictionary as a kwargs
#     new_blog = BlogTable(**request.dict(), member_id=1)
#     # Add the new blog to the Database
#     db.add(new_blog)
#     # Commit to the DB
#     db.commit()
#     # refresh the newly created blog to return this blog
#     db.refresh(new_blog)
#     # Return the newly created blog
#     return new_blog



# #  Get All blogs from DB
# @app.get('/blog', status_code=status.HTTP_200_OK, response_model=List[ShowBlog], tags=['blogs'])
# def get_blogs(db: Session = Depends(get_db)):
#     blogs = db.query(BlogTable).all()
#     # return all blogs
#     return blogs

# # Delete the blog
# @app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['blogs'])
# def delete_blog(id, db: Session = Depends(get_db)):
#     # Delete the blog
#     blog = db.query(BlogTable).filter(BlogTable.id == id).delete(synchronize_session=False)  # type: ignore
#     db.commit()
#     # return
#     return {f"Blog with id {id} has been deleted"}
    

# @app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['blogs'])
# def update_blog(id, request: Blog,db: Session = Depends(get_db)):
#     blog = db.query(BlogTable).filter(BlogTable.id == id)
    
#     # Check if blog is empty
#     if not blog.first():
#         raise HTTPException(status_code=404, detail=F"Blog with {id} not found")
    
#     else:
#         blog.update(request.dict())
#         # Commit the Transaction
#         db.commit()
#         # Return the request
#         return request.dict()






# @app.get('/blog/{id}', status_code=status.HTTP_200_OK, response_model=ShowBlog, tags=['blogs'])
# def get_specific_blog(id: int, db: Session = Depends(get_db)):
#     # Query the DB model for a specific blog
#     blog = db.query(BlogTable).filter(BlogTable.id == id).first()
#     if not blog:
#         raise HTTPException(status_code=404, detail=f"Blog with id {id} not found")
#     return blog




# @app.post('/user', status_code=status.HTTP_200_OK, response_model=ShowUser, tags=['users'])
# def create_user(request: User, db: Session = Depends(get_db)):
#     # Hash the Password
#     hashed_password = HashPassword(request.password)
#     # Create the user 
#     new_user = UserTable(name=request.name, email=request.email, password=hashed_password.get_hashed_password())
#     # Add the new user
#     db.add(new_user)
#     # Commit the transaction
#     db.commit()
#     # Refresh on User
#     db.refresh(new_user)
#     return new_user


# @app.get('/user/{id}', status_code=status.HTTP_200_OK, response_model=ShowUser, tags=['users'])
# def get_user(id: int, db: Session = Depends(get_db)):
#     user = db.query(UserTable).filter(UserTable.id == id).first()
#     if not user:
#         raise HTTPException(status_code=404, detail=f"User with id {id} not found")
#     return user
    