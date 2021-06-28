# 626. Exchange Seats
# Medium

# 481

# 315

# Add to List

# Share
# SQL Schema
# Mary is a teacher in a middle school and she has a table seat storing students' names and their corresponding seat ids.

# The column id is continuous increment.

# Mary wants to change seats for the adjacent students.

# Can you write a SQL query to output the result for Mary?

 

# +---------+---------+
# |    id   | student |
# +---------+---------+
# |    1    | Abbot   |
# |    2    | Doris   |
# |    3    | Emerson |
# |    4    | Green   |
# |    5    | Jeames  |
# +---------+---------+
# For the sample input, the output is:

# +---------+---------+
# |    id   | student |
# +---------+---------+
# |    1    | Doris   |
# |    2    | Abbot   |
# |    3    | Green   |
# |    4    | Emerson |
# |    5    | Jeames  |
# +---------+---------+
# Note:

# If the number of students is odd, there is no need to change the last one's seat.



S1
# Write your MySQL query statement below
with max_count as
(select count(*) as cnt
from seat)

select 
(case when mod(s.id, 2)!=0 and s.id != m.cnt then s.id+1
      when mod(s.id, 2)!=0 and s.id=m.cnt then s.id
      else s.id-1 end) as id,
      s.student
from seat s, max_count m
order by id
