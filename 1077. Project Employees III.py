# 1077. Project Employees III
# Medium
# 1292Add to ListShare
# SQL Schema
# Table: Project
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | project_id  | int     |
# | employee_id | int     |
# +-------------+---------+
# (project_id, employee_id) is the primary key of this table.
# employee_id is a foreign key to Employee table.
# Table: Employee
# +------------------+---------+
# | Column Name      | Type    |
# +------------------+---------+
# | employee_id      | int     |
# | name             | varchar |
# | experience_years | int     |
# +------------------+---------+
# employee_id is the primary key of this table.
 
# Write an SQL query that reports the most experienced employees in each project. In case of a tie, report all employees with the maximum number of experience years.
# The query result format is in the following example:
# Project table:
# +-------------+-------------+
# | project_id  | employee_id |
# +-------------+-------------+
# | 1           | 1           |
# | 1           | 2           |
# | 1           | 3           |
# | 2           | 1           |
# | 2           | 4           |
# +-------------+-------------+

# Employee table:
# +-------------+--------+------------------+
# | employee_id | name   | experience_years |
# +-------------+--------+------------------+
# | 1           | Khaled | 3                |
# | 2           | Ali    | 2                |
# | 3           | John   | 3                |
# | 4           | Doe    | 2                |
# +-------------+--------+------------------+

# Result table:
# +-------------+---------------+
# | project_id  | employee_id   |
# +-------------+---------------+
# | 1           | 1             |
# | 1           | 3             |
# | 2           | 1             |
# +-------------+---------------+
# Both employees with id 1 and 3 have the most experience among the employees of the first project. For the second project, the employee with id 1 has the most experience.


# Write your MySQL query statement below

select t1.project_id, t1.employee_id
from (
select t.project_id, t.employee_id, rank() over(partition by t.project_id order by experience_years desc) as rnk from 
(
select p.project_id, p.employee_id, e.experience_years from Project p
 left join
Employee e
on p.employee_id =e.employee_id
) t 
) t1
where t1.rnk =1
