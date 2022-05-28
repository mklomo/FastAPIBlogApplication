from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def index():
    return {"data" : {"name": "value"}}


@app.get("/about")
def about():
    return {"data" : ["value1", "value2"]}