# 1613. Find the Missing IDs
# Medium

# 77

# 10

# Add to List

# Share
# SQL Schema
# Table: Customers

# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | customer_id   | int     |
# | customer_name | varchar |
# +---------------+---------+
# customer_id is the primary key for this table.
# Each row of this table contains the name and the id customer.
 

# Write an SQL query to find the missing customer IDs. The missing IDs are ones that are not in the Customers table but are in the range between 1 and the maximum customer_id present in the table.

# Notice that the maximum customer_id will not exceed 100.

# Return the result table ordered by ids in ascending order.

# The query result format is in the following example.

 

# Customers table:
# +-------------+---------------+
# | customer_id | customer_name |
# +-------------+---------------+
# | 1           | Alice         |
# | 4           | Bob           |
# | 5           | Charlie       |
# +-------------+---------------+

# Result table:
# +-----+
# | ids |
# +-----+
# | 2   |
# | 3   |
# +-----+
# The maximum customer_id present in the table is 5, so in the range [1,5], IDs 2 and 3 are missing from the table.


# Write your MySQL query statement below
with recursive id_table as 
(select 1 as customer_id 
union  
select customer_id +1 from id_table where customer_id +1 <= 
(select max(customer_id) from Customers))

select i.customer_id as ids from id_table i
where i.customer_id not in (select customer_id from Customers)
order by i.customer_id
