# 1164. Product Price at a Given Date
# Medium

# 158

# 38

# Add to List

# Share
# SQL Schema
# Table: Products

# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | product_id    | int     |
# | new_price     | int     |
# | change_date   | date    |
# +---------------+---------+
# (product_id, change_date) is the primary key of this table.
# Each row of this table indicates that the price of some product was changed to a new price at some date.
 

# Write an SQL query to find the prices of all products on 2019-08-16. Assume the price of all products before any change is 10.

# The query result format is in the following example:

# Products table:
# +------------+-----------+-------------+
# | product_id | new_price | change_date |
# +------------+-----------+-------------+
# | 1          | 20        | 2019-08-14  |
# | 2          | 50        | 2019-08-14  |
# | 1          | 30        | 2019-08-15  |
# | 1          | 35        | 2019-08-16  |
# | 2          | 65        | 2019-08-17  |
# | 3          | 20        | 2019-08-18  |
# +------------+-----------+-------------+

# Result table:
# +------------+-------+
# | product_id | price |
# +------------+-------+
# | 2          | 50    |
# | 1          | 35    |
# | 3          | 10    |
# +------------+-------+


# Write your MySQL query statement below

# S1
select distinct p3.product_id, 10 as price
from Products p3
group by p3.product_id
having(min(p3.change_date) > '2019-08-16')

union

select p1.product_id, p1.new_price as price 
from Products p1
where (p1.product_id, p1.change_date) in 
(select p.product_id, max(p.change_date) as change_date
from Products p
where p.change_date <='2019-08-16'
group by p.product_id) 

# S2

# Write your MySQL query statement below

select distinct p3.product_id, ifnull(p4.price, 10) as price
from Products p3
 left join 
(
select p1.product_id, p1.new_price as price 
from Products p1
where (p1.product_id, p1.change_date) in 
(select p.product_id, max(p.change_date) as change_date
from Products p
where p.change_date <='2019-08-16'
group by p.product_id) 
) p4
on p3.product_id = p4.product_id
