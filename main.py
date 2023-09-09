from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
from fastapi import Response, status, HTTPException


app = FastAPI()

class Post(BaseModel):
    tittle: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [{"tittle": "tittle of post 1", "content": "content of post 1", "rating": 6, "id": 1}, {"tittle":"Favourite foods", "content": "i like swallow", "id": 2}]

## Find Id
def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

## Find index
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            return i

@app.get("/")
def root():
    return {"message": "Welcome to my API"}

@app.get("/posts")
def get_post():
    return {"data": my_posts}

# @app.post("/create_posts")
# def create_posts(payload: dict = Body(...)):
#     print(payload)
#     return {"new_post": f"title {payload['tittle']}, content: {payload[ 'content']}"}

# @app.get("/posts")
# def get_post():
#     return {"data": my_posts}

## Passing BaseModel for validation
# @app.post("/posts")
# def create_posts(post: Post):
#     print(post.rating)
#     print(post.dict())
#     return {"data": post}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 100)
    my_posts.append(post_dict)
    return {"data": my_posts}

## Get Latest Post
@app.get("/posts/latest")
def get_latest():
    post = my_posts[len(my_posts) -1]
    return { "latest_post": post}

## retrieve single ITEM
@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"post with id: {id} was not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return f"post with id={3} not found"
    return {"post_detail": post}

## Delete a post

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} not exist")

    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
