# 184. Department Highest Salary
# Medium
# 682141Add to ListShare
# SQL Schema
# The Employee table holds all employees. Every employee has an Id, a salary, and there is also a column for the department Id.
# +----+-------+--------+--------------+
# | Id | Name  | Salary | DepartmentId |
# +----+-------+--------+--------------+
# | 1  | Joe   | 70000  | 1            |
# | 2  | Jim   | 90000  | 1            |
# | 3  | Henry | 80000  | 2            |
# | 4  | Sam   | 60000  | 2            |
# | 5  | Max   | 90000  | 1            |
# +----+-------+--------+--------------+
# The Department table holds all departments of the company.
# +----+----------+
# | Id | Name     |
# +----+----------+
# | 1  | IT       |
# | 2  | Sales    |
# +----+----------+
# Write a SQL query to find employees who have the highest salary in each of the departments. For the above tables, your SQL query should return the following rows (order of rows does not matter).
# +------------+----------+--------+
# | Department | Employee | Salary |
# +------------+----------+--------+
# | IT         | Max      | 90000  |
# | IT         | Jim      | 90000  |
# | Sales      | Henry    | 80000  |
# +------------+----------+--------+
# Explanation:
# Max and Jim both have the highest salary in the IT department and Henry has the highest salary in the Sales department.



Solution 1

Note* There are duplicated max salaries, we need to get around with this. 

select t2.Name as Department, t1.Name as Employee, t1.Salary as Salary 
from Employee t1
join Department t2
on t1.DepartmentId = t2.Id
where (t1.DepartmentId, t1.Salary) in 
(select DepartmentId, max(Salary) from Employee
group by DepartmentId)

Solution 2

Note* 反向思考，elementwise 找每个部门里比现有工资更大的工资个数，为0的就是最大值，也是绕开了多个duplicated max。

select t2.Name as Department, t1.Name as Employee, t1.Salary as Salary 
from Employee t1
join Department t2
on t1.DepartmentId = t2.Id
where (select count(distinct t3.Id) from Employee t3
      where t3.Salary >t1.Salary and t3.DepartmentId=t1.DepartmentId) = 0


Solution 3

Window function 

    select distinct
        d.name as Department,
        e.name as Employee,
        e.salary as salary
    from (
        select departmentid,id,name,salary,rank() over(partition by departmentid order by salary desc) as pm from employee
    ) e 
     join 
        department d 
    on 
        e.departmentid = d.id
where e.pm = 1
