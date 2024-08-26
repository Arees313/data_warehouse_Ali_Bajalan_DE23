SHOW DATABASES;


CREATE DATABASE IF NOT EXISTS demo_db;

USE DATABASE demo_db;

SHOW SCHEMAS;

CREATE SCHEMA IF NOT EXISTS demo_db.staging;

SHOW SCHEMAS IN demo_db;

CREATE TABLE IF NOT EXISTS customer (
    customer_id integer PRIMARY KEY,
    age integer,
    email varchar(50)


);

SHOW TABLES;

SELECT * FROM CUSTOMER;

INSERT INTO CUSTOMER (customer_id, age, email)
VALUES 
    (1, 32, 'ABC@gmail.com'),
    (2, 15, 'CBD@gmail.com'),
    (3, 11, 'GFD@gmail.com');



DROP DATABASE demo_db;

SHOW DATABASES;