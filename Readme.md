## Fast API

### Fast api help website

- https://fastapi.tiangolo.com/#requirements

Create Virtual Environment

pip3 -m venv venv

source venv/bin/activate

## Installing fast api

- pips install "fastapi[all]" 

Above command will install libraries for fastapi

## Start the server

uvicorn main:app --reload

- --reload will ensure the server is reloaded whenever you make changes on your code

## Path Operation to be aware of

- CRUD [ Create=Post, Read=Get, Update=Put, Delete=Delete]

## Using pydantic for data validation

Pydantic is the most widely used data validation library for Python.

- https://docs.pydantic.dev/latest/

- from pydantic import BaseModel

## Using HTTP Status Code

- https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

## Fast API built in support

- start the server

- hit http://localhost:8000/docs

## Adding src folder

-  create a folder e.g app or src folder

- move the main.py file inside it.

- Create a dummy file inside the folder " touch __init__.py " this will teun the file into python package

-restart the server  

- uvicorn app.main:app --reload

## Working with Database

- Datbase is a collection of organzed data can be easily accessed and managed

### Note:
You don't work or interact with database directly, instead we make use of software refferred to as a Database Management System (DBMS)

## Relational DBMS

- MYSQL

- POSTGRESQL

- ORACLE

- SQL SERVER

## N0SQL DBMS

- MongoDB

- DynamoDB

