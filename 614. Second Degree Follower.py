# 614. Second Degree Follower
# Medium

# 88

# 612

# Add to List

# Share
# SQL Schema
# In facebook, there is a follow table with two columns: followee, follower.

# Please write a sql query to get the amount of each follower’s follower if he/she has one.

# For example:

# +-------------+------------+
# | followee    | follower   |
# +-------------+------------+
# |     A       |     B      |
# |     B       |     C      |
# |     B       |     D      |
# |     D       |     E      |
# +-------------+------------+
# should output:
# +-------------+------------+
# | follower    | num        |
# +-------------+------------+
# |     B       |  2         |
# |     D       |  1         |
# +-------------+------------+
# Explaination:
# Both B and D exist in the follower list, when as a followee, B's follower is C and D, and D's follower is E. A does not exist in follower list.
 

 

# Note:
# Followee would not follow himself/herself in all cases.
# Please display the result in follower's alphabet order.


# Write your MySQL query statement below

with first_order as
(select followee, count( distinct follower) as cnt_flw
from follow
group by followee)

select distinct f1.follower, f2.cnt_flw as num from follow f1
join first_order f2
on f1.follower = f2.followee
group by f1.follower
order BY f1.follower

# we need to find the fisrt order follow relationship that is all name in followee and how many followers they have
# then we look up the first-order followee and map them in to follower and now their identification is follower
# folloee--->follower step1
# follower--->followee--->follower step 2
