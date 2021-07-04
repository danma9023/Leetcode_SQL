# 574. Winning Candidate
# Medium

# 91

# 344

# Add to List

# Share
# SQL Schema
# Table: Candidate

# +-----+---------+
# | id  | Name    |
# +-----+---------+
# | 1   | A       |
# | 2   | B       |
# | 3   | C       |
# | 4   | D       |
# | 5   | E       |
# +-----+---------+  
# Table: Vote

# +-----+--------------+
# | id  | CandidateId  |
# +-----+--------------+
# | 1   |     2        |
# | 2   |     4        |
# | 3   |     3        |
# | 4   |     2        |
# | 5   |     5        |
# +-----+--------------+
# id is the auto-increment primary key,
# CandidateId is the id appeared in Candidate table.
# Write a sql to find the name of the winning candidate, the above example will return the winner B.

# +------+
# | Name |
# +------+
# | B    |
# +------+
# Notes:

# You may assume there is no tie, in other words there will be only one winning candidate.


# Write your MySQL query statement below

select c.Name as name 
from Candidate c join (
select CandidateId, count(id) as cnt from Vote
group by CandidateId
order by cnt desc
limit 1 ) t
on c.id = t.CandidateId


# With a tie 

# Write your MySQL query statement below
with count_table as (
select CandidateId, count(id) as cnt from Vote
group by CandidateId
order by cnt desc)

select c.Name as name 
from Candidate c join (select cn.CandidateId, dense_rank() over(order by cn.cnt desc)
                        as rnk from count_table cn) t
on c.id = t.CandidateId
where t.rnk =1
