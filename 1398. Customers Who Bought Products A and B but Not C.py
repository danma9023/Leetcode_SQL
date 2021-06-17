# 1398. Customers Who Bought Products A and B but Not C
# Medium

# 102

# 4

# Add to List

# Share
# SQL Schema
# Table: Customers

# +---------------------+---------+
# | Column Name         | Type    |
# +---------------------+---------+
# | customer_id         | int     |
# | customer_name       | varchar |
# +---------------------+---------+
# customer_id is the primary key for this table.
# customer_name is the name of the customer.
 

# Table: Orders

# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | order_id      | int     |
# | customer_id   | int     |
# | product_name  | varchar |
# +---------------+---------+
# order_id is the primary key for this table.
# customer_id is the id of the customer who bought the product "product_name".
 

# Write an SQL query to report the customer_id and customer_name of customers who bought products "A", "B" but did not buy the product "C" since we want to recommend them buy this product.

# Return the result table ordered by customer_id.

# The query result format is in the following example.

 

# Customers table:
# +-------------+---------------+
# | customer_id | customer_name |
# +-------------+---------------+
# | 1           | Daniel        |
# | 2           | Diana         |
# | 3           | Elizabeth     |
# | 4           | Jhon          |
# +-------------+---------------+

# Orders table:
# +------------+--------------+---------------+
# | order_id   | customer_id  | product_name  |
# +------------+--------------+---------------+
# | 10         |     1        |     A         |
# | 20         |     1        |     B         |
# | 30         |     1        |     D         |
# | 40         |     1        |     C         |
# | 50         |     2        |     A         |
# | 60         |     3        |     A         |
# | 70         |     3        |     B         |
# | 80         |     3        |     D         |
# | 90         |     4        |     C         |
# +------------+--------------+---------------+

# Result table:
# +-------------+---------------+
# | customer_id | customer_name |
# +-------------+---------------+
# | 3           | Elizabeth     |
# +-------------+---------------+
# Only the customer_id with id 3 bought the product A and B but not the product C.


# Write your MySQL query statement below

select t.customer_id, t.customer_name from
(
select c.customer_id, c.customer_name,
sum(case when o.product_name = 'A' then 1 else 0 end) as a_buy,
sum(case when o.product_name = 'B' then 1 else 0 end) as b_buy,
sum(case when o.product_name = 'C' then 1 else 0 end) as c_buy
from Customers c left join Orders o
on c.customer_id = o.customer_id
group by c.customer_id
) t 
where t.a_buy > 0 and t.b_buy>0 and t.c_buy=0
order by t.customer_id
