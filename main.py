from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Working with W=Query Parameters
@app.get("/blog")
def index(limit = 10, published : bool = True, sort: Optional[str] = None):
    # Only get 10 published blogs
    if published:
        return {"data" : f"{limit} published blogs"}
    
    else:
        return {"data" : f"{limit} blogs"}


@app.get("/about")
def about():
    return {"data" : ["value1", "value2"]}



class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]
    
    



@app.post("/blog")
def create_blog(request: Blog):
    return {'data' : 'blog created'}



# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=9000)