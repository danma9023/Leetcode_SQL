# 1454. Active Users
# Medium

# 186

# 22

# Add to List

# Share
# SQL Schema
# Table Accounts:

# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | id            | int     |
# | name          | varchar |
# +---------------+---------+
# the id is the primary key for this table.
# This table contains the account id and the user name of each account.
 

# Table Logins:

# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | id            | int     |
# | login_date    | date    |
# +---------------+---------+
# There is no primary key for this table, it may contain duplicates.
# This table contains the account id of the user who logged in and the login date. A user may log in multiple times in the day.
 

# Write an SQL query to find the id and the name of active users.

# Active users are those who logged in to their accounts for 5 or more consecutive days.

# Return the result table ordered by the id.

# The query result format is in the following example:

# Accounts table:
# +----+----------+
# | id | name     |
# +----+----------+
# | 1  | Winston  |
# | 7  | Jonathan |
# +----+----------+

# Logins table:
# +----+------------+
# | id | login_date |
# +----+------------+
# | 7  | 2020-05-30 |
# | 1  | 2020-05-30 |
# | 7  | 2020-05-31 |
# | 7  | 2020-06-01 |
# | 7  | 2020-06-02 |
# | 7  | 2020-06-02 |
# | 7  | 2020-06-03 |
# | 1  | 2020-06-07 |
# | 7  | 2020-06-10 |
# +----+------------+

# Result table:
# +----+----------+
# | id | name     |
# +----+----------+
# | 7  | Jonathan |
# +----+----------+
# User Winston with id = 1 logged in 2 times only in 2 different days, so, Winston is not an active user.
# User Jonathan with id = 7 logged in 7 times in 6 different days, five of them were consecutive days, so, Jonathan is an active user.
# Follow up question:
# Can you write a general solution if the active users are those who logged in to their accounts for n or more consecutive days?


# S1

with 
uniq as 
(select distinct id, login_date from Logins), 
lead_t as 
(select *, lead(login_date, 4) over(partition by id order by login_date) as l_date from uniq)

select distinct a.id, a.name from Accounts a,
lead_t l 
where a.id= l.id
and datediff(l.l_date, l.login_date) = 4
order by l.id

# S2

select distinct l1.id, (select a.name from Accounts a where a.id= l1.id ) as name 
from Logins l1, Logins l2
where l1.id = l2.id 
and datediff(l1.login_date, l2.login_date) between 1 and 4
group by l1.id, l1.login_date
having count(distinct l2.login_date) = 4
order by l1.id
