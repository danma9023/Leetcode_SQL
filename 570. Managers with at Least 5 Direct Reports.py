# 570. Managers with at Least 5 Direct Reports
# Medium

# 153

# 20

# Add to List

# Share
# SQL Schema
# The Employee table holds all employees including their managers. Every employee has an Id, and there is also a column for the manager Id.

# +------+----------+-----------+----------+
# |Id    |Name 	  |Department |ManagerId |
# +------+----------+-----------+----------+
# |101   |John 	  |A 	      |null      |
# |102   |Dan 	  |A 	      |101       |
# |103   |James 	  |A 	      |101       |
# |104   |Amy 	  |A 	      |101       |
# |105   |Anne 	  |A 	      |101       |
# |106   |Ron 	  |B 	      |101       |
# +------+----------+-----------+----------+
# Given the Employee table, write a SQL query that finds out managers with at least 5 direct report. For the above table, your SQL query should return:

# +-------+
# | Name  |
# +-------+
# | John  |
# +-------+
# Note:
# No one would report to himself.


# S1

# Write your MySQL query statement below

select e1.name from Employee e1
where e1.Id in (
select ManagerId from Employee
group by ManagerId
having count(Id) >=5 ) 


# S2

# Write your MySQL query statement below

select e1.name from Employee e1
join (
select ManagerId from Employee
group by ManagerId
having count(Id) >=5 ) e2
on e1.Id = e2.ManagerId
