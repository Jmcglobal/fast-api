## Fast API

### Fast api help website

- https://fastapi.tiangolo.com/#requirements

Create Virtual Environment

pip3 -m venv venv

source venv/bin/activate

#### Installing fast api

- pips install "fastapi[all]" 

Above command will install libraries for fastapi

#### Start the server

uvicorn main:app --reload

- --reload will ensure the server is reloaded whenever you make changes on your code

#### Path Operation to be aware of

- CRUD [ Create=Post, Read=Get, Update=Put, Delete=Delete]

#### Using pydantic for data validation

Pydantic is the most widely used data validation library for Python.

- https://docs.pydantic.dev/latest/

- from pydantic import BaseModel

#### Using HTTP Status Code

- https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

#### Fast API built in support

- start the server

- hit http://localhost:8000/docs

#### Adding src folder

-  create a folder e.g app or src folder

- move the main.py file inside it.

- Create a dummy file inside the folder " touch __init__.py " this will teun the file into python package

-restart the server  

- uvicorn app.main:app --reload

#### Working with Database

- Datbase is a collection of organzed data can be easily accessed and managed

#### Note:
You don't work or interact with database directly, instead we make use of software refferred to as a Database Management System (DBMS)

#### Relational DBMS

- MYSQL

- POSTGRESQL

- ORACLE

- SQL SERVER

#### N0SQL DBMS

- MongoDB

- DynamoDB

#### Installing Postgres on Mac

- https://www.postgresql.org/

- click on download

- select macOS

- Follow installation guide on the platform

- Installing with EDB 

- The following package will be installed

-       PostgreSQL Server
-       pgAdmin
-       Stack Builder
-       Command Line Tools

- Set password "admin"

- Default port 5432

- Database Superuser =  postgres

#### Working DAtabase Tables

- A table represent a subject or event in an application

#### Columns Vs Rows

- A table is made up of columns and rows

- Each Column represents a different attribute

- Each row represent a different entry in the table

##### Postgres DataTypes

- Numeric = int, decimal, precision

- Text = Varchar, text

- bool = boolean

- sequence = array

#### Primary Key

- A column or group of columns that uniquely identifies each row in a table

- Table can have one and only one primary key

- It is up to you to decide to decide which column to use as primary key, for example "email" and "Phone Number"

        email column will always be uniqque no duplicate
        Phone Number will always be unique, two users cannot have the same email and phone number

#### Unique Constraints

- A unique constraint can be applied to any column to make sure every record has a unique value for that column

- Example: maybe if your email column is primary key, and you want to make sure phone number column has no duplicate, unique constraint will help to fix it.

#### Null Constraint

- by default, when adding a new entry to a database, any colunm can be left blank. When a column is left blank, it has a null value

- If you need a colum to be properly filled in to create a new record, a NOT NULL constraint can be added to the column to ensure that the column is never left blank

#### COMMON SQL OPERATOR COMMAND

- Create Table

    CREATE DATABASE student;

- Select all table columes and rows oder by ascending order

    SELECT * FROM products ORDER by id ASC;

- Select every entry on the products table

    SELECT * FROM products;

- Select name column

    SELECT name FROM products;

- Select multiple columns

    SELECT name, id, price FROM products;

#### FILTERING

    SELECT * FROM products WHERE inventory = 0;
    SELECT * FROM products WHERE id = 1;
    SELECT * FROM products WHERE name = 'TV';
    SELECT * FROM products WHERE price > 200 AND price < 1000;
    SELECT * FROM products WHERE price > 100 OR price < 200;
    SELECT * FROM products WHERE id IN (1,2,6);
    SELECT * FROM products WHERE name LIKE 'TV%';
    SELECT * FROM products ORDER BY price ASC;
    SELECT * FROM products ORDER BY price DESC;

#### ADDING AN ENTRY

    INSERT INTO products (name, price, inventory) VALUES ('benz', 3000, 201);

#### ADDING ENTRY and Returning Inserted values

    INSERT INTO products (name, price, inventory) VALUES ('benz', 3000, 201) returning *;

#### UPDATE ENTRY

    UPDATE products SET name = 'flower', price = 333 WHERE id = 25

#### CREATE DATABASE FOR POSTS And Connecting to Python

- https://www.psycopg.org/docs/

#### Installing  psycopg2-binary

- pip3 install psycopg2-binary

- import psycopg2

