# 1112. Highest Grade For Each Student
# Similar to 184. Department Highest Salary*********
# Medium

# 126

# 4

# Add to List

# Share
# SQL Schema
# Table: Enrollments

# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | student_id    | int     |
# | course_id     | int     |
# | grade         | int     |
# +---------------+---------+
# (student_id, course_id) is the primary key of this table.

# Write a SQL query to find the highest grade with its corresponding course for each student. In case of a tie, you should find the course with the smallest course_id. The output must be sorted by increasing student_id.

# The query result format is in the following example:

# Enrollments table:
# +------------+-------------------+
# | student_id | course_id | grade |
# +------------+-----------+-------+
# | 2          | 2         | 95    |
# | 2          | 3         | 95    |
# | 1          | 1         | 90    |
# | 1          | 2         | 99    |
# | 3          | 1         | 80    |
# | 3          | 2         | 75    |
# | 3          | 3         | 82    |
# +------------+-----------+-------+

# Result table:
# +------------+-------------------+
# | student_id | course_id | grade |
# +------------+-----------+-------+
# | 1          | 2         | 99    |
# | 2          | 2         | 95    |
# | 3          | 3         | 82    |
# +------------+-----------+-------+




# Write your MySQL query statement below

select e.student_id, min(e.course_id) as course_id, e.grade
from Enrollments e
where (e.student_id, e.grade) in
(
select student_id, max(grade) as max_grade
from Enrollments
group by student_id
) 
group by e.student_id
order by e.student_id


# S2
# Write your MySQL query statement below

select e.student_id, min(e.course_id) as course_id, e.grade
from 
(
select *, rank() over(partition by student_id order by grade desc) as grade_rank
    from Enrollments
) e
where e.grade_rank = 1
group by e.student_id
order by e.student_id
