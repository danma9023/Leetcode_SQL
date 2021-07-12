# 1459. Rectangles Area
# Medium

# 38

# 62

# Add to List

# Share
# SQL Schema
# Table: Points

# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | id            | int     |
# | x_value       | int     |
# | y_value       | int     |
# +---------------+---------+
# id is the primary key for this table.
# Each point is represented as a 2D coordinate (x_value, y_value).
 

# Write an SQL query to report all possible axis-aligned rectangles with non-zero area that can be formed by any two points in the Points table.

# Each row in the result should contain three columns (p1, p2, area) where:

# p1 and p2 are the id's of the two points that determine the opposite corners of a rectangle.
# area is the area of the rectangle and must be non-zero.
# Report the query in descending order by area first, then in ascending order by p1's id if there is a tie, then in ascending order by p2's id if there is another tie.

# The query result format is in the following table:



# Points table:
# +----------+-------------+-------------+
# | id       | x_value     | y_value     |
# +----------+-------------+-------------+
# | 1        | 2           | 7           |
# | 2        | 4           | 8           |
# | 3        | 2           | 10          |
# +----------+-------------+-------------+

# Result table:
# +----------+-------------+-------------+
# | p1       | p2          | area        |
# +----------+-------------+-------------+
# | 2        | 3           | 4           |
# | 1        | 2           | 2           |
# +----------+-------------+-------------+


# The rectangle formed by p1 = 2 and p2 = 3 has an area equal to |4-2| * |8-10| = 4.
# The rectangle formed by p1 = 1 and p2 = 2 has an area equal to |2-4| * |7-8| = 2.
# Note that the rectangle formed by p1 = 1 and p2 = 3 is invalid because the area is 0.


# Write your MySQL query statement below
select * from (
select po1.id as p1, po2.id as p2, (abs(po1.x_value-po2.x_value)*abs(po1.y_value-po2.y_value)) as area
from Points po1 left join Points po2
on po1.id < po2.id ) t
where t.area !=0 
order by t.area desc, t.p1, t.p2
