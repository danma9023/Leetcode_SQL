# 180. Consecutive Numbers
# Medium
# 666148Add to ListShare
# SQL Schema
# Table: Logs
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | num         | varchar |
# +-------------+---------+
# id is the primary key for this table.
 
# Write an SQL query to find all numbers that appear at least three times consecutively.
# Return the result table in any order.
# The query result format is in the following example:
 
# Logs table:
# +----+-----+
# | Id | Num |
# +----+-----+
# | 1  | 1   |
# | 2  | 1   |
# | 3  | 1   |
# | 4  | 2   |
# | 5  | 1   |
# | 6  | 2   |
# | 7  | 2   |
# +----+-----+

# Result table:
# +-----------------+
# | ConsecutiveNums |
# +-----------------+
# | 1               |
# +-----------------+
# 1 is the only number that appears consecutively for at least three times.


# Write your MySQL query statement below

select  distinct l1.Num as ConsecutiveNums from Logs l1 , Logs l2, Logs l3
where l1.Num = l2.Num and l2.Num = l3.Num 
and l1.Id +1 = l2.Id and l2.Id +1 =l3.Id
