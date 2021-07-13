# 1715. Count Apples and Oranges
# Medium

# 33

# 5

# Add to List

# Share
# SQL Schema
# Table: Boxes

# +--------------+------+
# | Column Name  | Type |
# +--------------+------+
# | box_id       | int  |
# | chest_id     | int  |
# | apple_count  | int  |
# | orange_count | int  |
# +--------------+------+
# box_id is the primary key for this table.
# chest_id is a foreign key of the chests table.
# This table contains information about the boxes and the number of oranges and apples they contain. Each box may contain a chest, which also can contain oranges and apples.
 

# Table: Chests

# +--------------+------+
# | Column Name  | Type |
# +--------------+------+
# | chest_id     | int  |
# | apple_count  | int  |
# | orange_count | int  |
# +--------------+------+
# chest_id is the primary key for this table.
# This table contains information about the chests we have, and the corresponding number if oranges and apples they contain.
 

# Write an SQL query to count the number of apples and oranges in all the boxes. If a box contains a chest, you should also include the number of apples and oranges it has.

# Return the result table in any order.

# The query result format is in the following example:

 

# Boxes table:
# +--------+----------+-------------+--------------+
# | box_id | chest_id | apple_count | orange_count |
# +--------+----------+-------------+--------------+
# | 2      | null     | 6           | 15           |
# | 18     | 14       | 4           | 15           |
# | 19     | 3        | 8           | 4            |
# | 12     | 2        | 19          | 20           |
# | 20     | 6        | 12          | 9            |
# | 8      | 6        | 9           | 9            |
# | 3      | 14       | 16          | 7            |
# +--------+----------+-------------+--------------+

# Chests table:
# +----------+-------------+--------------+
# | chest_id | apple_count | orange_count |
# +----------+-------------+--------------+
# | 6        | 5           | 6            |
# | 14       | 20          | 10           |
# | 2        | 8           | 8            |
# | 3        | 19          | 4            |
# | 16       | 19          | 19           |
# +----------+-------------+--------------+

# Result table:
# +-------------+--------------+
# | apple_count | orange_count |
# +-------------+--------------+
# | 151         | 123          |
# +-------------+--------------+
# box 2 has 6 apples and 15 oranges.
# box 18 has 4 + 20 (from the chest) = 24 apples and 15 + 10 (from the chest) = 25 oranges.
# box 19 has 8 + 19 (from the chest) = 27 apples and 4 + 4 (from the chest) = 8 oranges.
# box 12 has 19 + 8 (from the chest) = 27 apples and 20 + 8 (from the chest) = 28 oranges.
# box 20 has 12 + 5 (from the chest) = 17 apples and 9 + 6 (from the chest) = 15 oranges.
# box 8 has 9 + 5 (from the chest) = 14 apples and 9 + 6 (from the chest) = 15 oranges.
# box 3 has 16 + 20 (from the chest) = 36 apples and 7 + 10 (from the chest) = 17 oranges.
# Total number of apples = 6 + 24 + 27 + 27 + 17 + 14 + 36 = 151
# Total number of oranges = 15 + 25 + 8 + 28 + 15 + 15 + 17 = 123


# Write your MySQL query statement below
with all_count as 
(select b.*, ifnull(c.apple_count, 0) as chest_apple, ifnull(c.orange_count, 0) as chest_orange
from Boxes b left join Chests c
on b.chest_id = c.chest_id)

# select sum(t.apple_box) as apple_count, 
# sum(orange_box) as orange_count 
# from (
select sum(a.apple_count) + sum(a.chest_apple) as  apple_count,
 sum(a.orange_count) + sum(a.chest_orange) as orange_count from all_count a
 # group by a.box_id
  # ) t
