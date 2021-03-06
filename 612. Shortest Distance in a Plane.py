# 612. Shortest Distance in a Plane
# Medium

# 128

# 44

# Add to List

# Share
# SQL Schema
# Table point_2d holds the coordinates (x,y) of some unique points (more than two) in a plane.
 

# Write a query to find the shortest distance between these points rounded to 2 decimals.
 

# | x  | y  |
# |----|----|
# | -1 | -1 |
# | 0  | 0  |
# | -1 | -2 |
 

# The shortest distance is 1.00 from point (-1,-1) to (-1,2). So the output should be:
 

# | shortest |
# |----------|
# | 1.00     |


# S1
# Write your MySQL query statement below
SELECT
    ROUND(SQRT(MIN((POW(p1.x - p2.x, 2) + POW(p1.y - p2.y, 2)))),2) AS shortest
FROM
    point_2d p1
        JOIN
    point_2d p2 ON (p1.x <= p2.x AND p1.y < p2.y)
        OR (p1.x <= p2.x AND p1.y > p2.y)
        OR (p1.x < p2.x AND p1.y = p2.y)
        
# S2
select 
round(sqrt(min(pow(p1.x-p2.x, 2)+pow(p1.y-p2.y, 2))), 2) as shortest
from point_2d p1
 join 
 #the distance is mutural, so we use inner join
point_2d p2
on p1.x!=p2.x or p1.y!=p2.y
