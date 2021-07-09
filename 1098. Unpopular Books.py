# 1098. Unpopular Books
# Medium
# 104253Add to ListShare
# SQL Schema
# Table: Books
# +----------------+---------+
# | Column Name    | Type    |
# +----------------+---------+
# | book_id        | int     |
# | name           | varchar |
# | available_from | date    |
# +----------------+---------+
# book_id is the primary key of this table.
# Table: Orders
# +----------------+---------+
# | Column Name    | Type    |
# +----------------+---------+
# | order_id       | int     |
# | book_id        | int     |
# | quantity       | int     |
# | dispatch_date  | date    |
# +----------------+---------+
# order_id is the primary key of this table.
# book_id is a foreign key to the Books table.
 
# Write an SQL query that reports the books that have sold less than 10 copies in the last year, excluding books that have been available for less than 1 month from today. Assume today is 2019-06-23.
# The query result format is in the following example:
# Books table:
# +---------+--------------------+----------------+
# | book_id | name               | available_from |
# +---------+--------------------+----------------+
# | 1       | "Kalila And Demna" | 2010-01-01     |
# | 2       | "28 Letters"       | 2012-05-12     |
# | 3       | "The Hobbit"       | 2019-06-10     |
# | 4       | "13 Reasons Why"   | 2019-06-01     |
# | 5       | "The Hunger Games" | 2008-09-21     |
# +---------+--------------------+----------------+

# Orders table:
# +----------+---------+----------+---------------+
# | order_id | book_id | quantity | dispatch_date |
# +----------+---------+----------+---------------+
# | 1        | 1       | 2        | 2018-07-26    |
# | 2        | 1       | 1        | 2018-11-05    |
# | 3        | 3       | 8        | 2019-06-11    |
# | 4        | 4       | 6        | 2019-06-05    |
# | 5        | 4       | 5        | 2019-06-20    |
# | 6        | 5       | 9        | 2009-02-02    |
# | 7        | 5       | 8        | 2010-04-13    |
# +----------+---------+----------+---------------+

# Result table:
# +-----------+--------------------+
# | book_id   | name               |
# +-----------+--------------------+
# | 1         | "Kalila And Demna" |
# | 2         | "28 Letters"       |
# | 5         | "The Hunger Games" |
# +-----------+--------------------+

# S1


with book1 as
(select b.book_id, b.name from Books b
where datediff('2019-06-23', b.available_from) > 30),

order1 as 
(select o.book_id, o.quantity from Orders o
where o.dispatch_date > date_sub('2019-06-23', interval 1 year)
),
table1 as (
select b.book_id, b.name, o.quantity from 
book1 b
left join order1 o
on b.book_id = o.book_id
)

select t.book_id, t.name from table1 t 
group by t.book_id
having ifnull(sum(t.quantity), 0) < 10

# S1-shorter 



select t1.book_id, t1.name from 

(select b.book_id, b.name from Books b
where datediff('2019-06-23', b.available_from) > 30)
    t1

left join

(select o.book_id, o.quantity from Orders o
where o.dispatch_date > date_sub('2019-06-23', interval 1 year)) t2

on t1.book_id = t2.book_id 


group by t1.book_id 
having ifnull(sum(t2.quantity), 0) < 10

# S2 

select b.book_id, b.name from Books b
left join  Orders o
on o.book_id = b.book_id
and o.dispatch_date between '2018-06-23' and '2019-06-23'
where datediff('2019-06-23', b.available_from) > 30
group by b.book_id
having ifnull(sum(o.quantity), 0) < 10

