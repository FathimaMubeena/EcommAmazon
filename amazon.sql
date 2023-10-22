CREATE DATABASE amazon;
use amazon;

CREATE TABLE customers (
    username varchar(255) NOT NULL ,
    password varchar(255) NOT NULL ,
    customer_id int AUTO_INCREMENT PRIMARY KEY,
    first_name varchar(255) NOT NULL,
    last_name varchar(255) ,
    age int(2) NOT NULL,
    address varchar(255) NOT NULL,
    phone_number Int(10),
    credit_card Int(32),
    email_address varchar(255)
);

insert into customers
    (username, password, first_name, last_name, age, address, phone_number, credit_card, email_address)
 VALUES
    ("fathima123","123654","fathima","shaik",27,"west_park",501951,123789,"fmshaik@gmail.com"),
    ("mudasserO5","123","mohaammed","shaik",30,"belmont",3678,354664,"mudasser@gmail.com");


CREATE table products (
    product_id varchar(255) NOT NULL ,
    product_name varchar(255) NOT NULL ,
    category varchar(255) NOT NULL ,
    description varchar(255) NOT NULL ,
    price float,
    quantity Int NOT NULL DEFAULT 0,
    freeshiping BOOLEAN DEFAULT 0
);

INSERT into products
    (product_id, product_name, category, description, price,quantity,freeshiping)
values
    ("1001","soda","beverages","coca cola", 1.50,15,true),
    ("1002","milk","dairy","clover 12ml", 3.50,10,true);

-- login verify
SELECT * FROM customers WHERE username = 'fathima123' AND password = '123654' ;

-- What are the Total Stock quantity in Products ?
select sum(quantity) From products;

-- What is the Average by Category ?
select category, AVG(PRICE) From products GROUP BY CATEGORY;

-- Most Expensive and Least Expensive products ?
select product_name, price from  products where price =(select max(price) from products);
select product_name, price from  products where price =(select min(price) from products);

-- Count of products per (in each) Category ?
select Category, count(*) from products GROUP BY Category;

-- Price range Analysis
SELECT MIN(price), MAX(price) FROM products;


-- update Quantity

UPDATE products
SET quantity = 10
    WHERE product_id = '1001';

