from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to my API"}

@app.get("/post")
def get_post():
    return {"data": "This is your post"}

@app.post("/create_posts")
def create_posts(payload: dict = Body(...)):
    print(payload)
    return {"new_post": f"title {payload['tittle']}, content: {payload[ 'content']}"}