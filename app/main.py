from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
from fastapi import Response, status, HTTPException
import psycopg2
from psycopg2.extras import RealDictCursor
import time


app = FastAPI()

class Post(BaseModel):
    tittle: str
    content: str
    published: bool = True
    rating: Optional[int] = None
while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', port=5432,
        user='postgres', password='admin', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successfull")
        break
    except Exception as error:
        print("Connecting to database failed")
        print("Error: ", error)
        time.sleep(4)

# Hard coding post in a variable "my_posts" if their no database to save all post
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
    cursor.execute(""" SELECT * FROM posts """)
    posts = cursor.fetchall()
    return {"data": posts}

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
    cursor.execute(""" INSERT INTO posts (tittle, content, published) VALUES (%s, %s, %s) RETURNING * """, 
            (post.tittle, post.content, post.published))
    new_posts = cursor.fetchone()
    conn.commit()
    return {"data": new_posts}

## Get Latest Post
@app.get("/posts/latest")
def get_latest():
    post = my_posts[len(my_posts) -1]
    return { "latest_post": post}

## retrieve single ITEM
@app.get("/posts/{id}")
def get_post(id: str):
    cursor.execute(""" SELECT * FROM posts WHERE id = %s """, (str(id),))
    post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"post with id: {id} was not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return f"post with id={3} not found"
    return {"post_detail": post}

## Delete a post

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: str):
    cursor.execute(""" DELETE FROM posts WHERE id = %s returning *""", (str(id),))
    deleted_post = cursor.fetchone()
    conn.commit()
    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} not exist")

    return Response(status_code=status.HTTP_204_NO_CONTENT)

## Update a post

@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    cursor.execute(""" UPDATE posts SET tittle = %s, content = %s, published = %s WHERE  id = %s RETURNING *""", 
    (post.tittle, post.content, post.published, str(id)) )
    update_post = cursor.fetchone()
    conn.commit()
    if update_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} not exist")
    # post_dict = post.dict()
    # post_dict["id"] = id
    return {"message": update_post}