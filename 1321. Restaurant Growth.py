# 1321. Restaurant Growth
# Medium

# 171

# 25

# Add to List

# Share
# SQL Schema
# Table: Customer

# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | customer_id   | int     |
# | name          | varchar |
# | visited_on    | date    |
# | amount        | int     |
# +---------------+---------+
# (customer_id, visited_on) is the primary key for this table.
# This table contains data about customer transactions in a restaurant.
# visited_on is the date on which the customer with ID (customer_id) have visited the restaurant.
# amount is the total paid by a customer.
 

# You are the restaurant owner and you want to analyze a possible expansion (there will be at least one customer every day).

# Write an SQL query to compute moving average of how much customer paid in a 7 days window (current day + 6 days before) .

# The query result format is in the following example:

# Return result table ordered by visited_on.

# average_amount should be rounded to 2 decimal places, all dates are in the format ('YYYY-MM-DD').

 

# Customer table:
# +-------------+--------------+--------------+-------------+
# | customer_id | name         | visited_on   | amount      |
# +-------------+--------------+--------------+-------------+
# | 1           | Jhon         | 2019-01-01   | 100         |
# | 2           | Daniel       | 2019-01-02   | 110         |
# | 3           | Jade         | 2019-01-03   | 120         |
# | 4           | Khaled       | 2019-01-04   | 130         |
# | 5           | Winston      | 2019-01-05   | 110         | 
# | 6           | Elvis        | 2019-01-06   | 140         | 
# | 7           | Anna         | 2019-01-07   | 150         |
# | 8           | Maria        | 2019-01-08   | 80          |
# | 9           | Jaze         | 2019-01-09   | 110         | 
# | 1           | Jhon         | 2019-01-10   | 130         | 
# | 3           | Jade         | 2019-01-10   | 150         | 
# +-------------+--------------+--------------+-------------+

# Result table:
# +--------------+--------------+----------------+
# | visited_on   | amount       | average_amount |
# +--------------+--------------+----------------+
# | 2019-01-07   | 860          | 122.86         |
# | 2019-01-08   | 840          | 120            |
# | 2019-01-09   | 840          | 120            |
# | 2019-01-10   | 1000         | 142.86         |
# +--------------+--------------+----------------+

# 1st moving average from 2019-01-01 to 2019-01-07 has an average_amount of (100 + 110 + 120 + 130 + 110 + 140 + 150)/7 = 122.86
# 2nd moving average from 2019-01-02 to 2019-01-08 has an average_amount of (110 + 120 + 130 + 110 + 140 + 150 + 80)/7 = 120
# 3rd moving average from 2019-01-03 to 2019-01-09 has an average_amount of (120 + 130 + 110 + 140 + 150 + 80 + 110)/7 = 120
# 4th moving average from 2019-01-04 to 2019-01-10 has an average_amount of (130 + 110 + 140 + 150 + 80 + 110 + 130 + 150)/7 = 142.86

# Solution



# /* Write your T-SQL query statement below */
with temp as 
(select visited_on, sum(amount) as amount from 
 Customer
group by visited_on)
 
# Window Function

select t1.visited_on, t1.amount, round(t1.average_amount, 2) as average_amount
from 
(
select t.visited_on, sum(t.amount) over(order by t.visited_on rows between 6 preceding and current row)as amount,
avg(t.amount) over(order by t.visited_on rows between 6 preceding and current row) as average_amount
from temp t
) t1
where datediff(t1.visited_on, (select min(visited_on) from Customer)) >=6
group by t1.visited_on


# Cross Join (no key needed)
# For each row in table A, all rows from table B will join
# Note that we sum on the table B as a secondary table that is joined to table A

select t1.visited_on, sum(t2.amount) as amount, round(sum(t2.amount)/7, 2) as average_amount
from temp t1 cross join temp t2
where datediff(t1.visited_on, t2.visited_on) < 7
and t1.visited_on >= t2.visited_on
group by t1.visited_on
having count(*) > 6


/* Write your T-SQL query statement below */
with temp as 
(select visited_on, sum(amount) as amount from 
 Customer
group by visited_on)
 
# Inner Join (no key needed)
# Note that we sum on the table B as a secondary table that is joined to table A


select t1.visited_on, sum(c.amount) as amount, round(sum(c.amount)/7, 2) as average_amount
from temp t1  join Customer c
on t1.visited_on >= c.visited_on 
# accumulate date for each date
and t1.visited_on <= date_add(c.visited_on, interval 6 day)
and t1.visited_on >= date_add((select min(visited_on) from Customer), interval 6 day)
group by t1.visited_on
