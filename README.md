Question: create a flask api.route(/uploadProducts) where it loads the products.csv file and save it in the mysql database products

```
CREATE table products (
product_id varchar(255) NOT NULL ,
product_name varchar(255) NOT NULL ,
category varchar(255) NOT NULL ,
description varchar(255) NOT NULL ,
price float,
quantity Int NOT NULL DEFAULT 0,
freeshiping BOOLEAN DEFAULT 0
);
```

Answer :  ???

Question: create a flask api.route(/display_products) where it load the data from mysql products table and display in the html ?
 Answer : 

mysql> select * from products;
+------------+--------------------------------+----------------+----------------------+-------+----------+-------------+
| product_id | product_name                   | category       | description          | price | quantity | freeshiping |
+------------+--------------------------------+----------------+----------------------+-------+----------+-------------+
| 1001       | soda                           | beverages      | coca cola            |   1.5 |       15 |           1 |
| 1002       | milk                           | dairy          | clover 12ml          |   3.5 |       10 |           1 |
| 1001       |  Bottled Water                 |  Beverages     |  Aquafina            |  1.99 |      200 |           1 |
| 1002       |  Soda (12 oz)                  |  Beverages     |  Coca-Cola           |  1.49 |      150 |           1 |
.....
.....
+------------+--------------------------------+----------------+----------------------+-------+----------+-------------+

