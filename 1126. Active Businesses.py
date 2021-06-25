1126. Active Businesses
Medium

134

14

Add to List

Share
SQL Schema
Table: Events

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| business_id   | int     |
| event_type    | varchar |
| occurences    | int     | 
+---------------+---------+
(business_id, event_type) is the primary key of this table.
Each row in the table logs the info that an event of some type occured at some business for a number of times.
 

Write an SQL query to find all active businesses.

An active business is a business that has more than one event type with occurences greater than the average occurences of that event type among all businesses.

The query result format is in the following example:

Events table:
+-------------+------------+------------+
| business_id | event_type | occurences |
+-------------+------------+------------+
| 1           | reviews    | 7          |
| 3           | reviews    | 3          |
| 1           | ads        | 11         |
| 2           | ads        | 7          |
| 3           | ads        | 6          |
| 1           | page views | 3          |
| 2           | page views | 12         |
+-------------+------------+------------+

Result table:
+-------------+
| business_id |
+-------------+
| 1           |
+-------------+ 
Average for 'reviews', 'ads' and 'page views' are (7+3)/2=5, (11+7+6)/3=8, (3+12)/2=7.5 respectively.
Business with id 1 has 7 'reviews' events (more than 5) and 11 'ads' events (more than 8) so it is an active 


# Write your MySQL query statement below
select e.business_id
from 
(
select e2.business_id, e2.event_type, count(e2.event_type) as cnt from 
Events e2 
left join 
(
select e1.event_type, avg(e1.occurences) as avg_occ
from Events e1
group by e1.event_type
    ) e3
    
on e2.event_type = e3.event_type
where e2.occurences > e3.avg_occ
group by e2.business_id
) e
where e.cnt > 1



/* Write your T-SQL query statement below */
with temp_table 
as (
select *, avg(e1.occurences) over(partition by e1.event_type) as acg_occ
from Events e1)

select t.business_id from temp_table t
where t.occurences > t.acg_occ
group by t.business_id
having count(t.event_type) > 1
