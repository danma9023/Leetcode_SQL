# 1783. Grand Slam Titles
# Medium

# 53

# 0

# Add to List

# Share
# SQL Schema
# Table: Players

# +----------------+---------+
# | Column Name    | Type    |
# +----------------+---------+
# | player_id      | int     |
# | player_name    | varchar |
# +----------------+---------+
# player_id is the primary key for this table.
# Each row in this table contains the name and the ID of a tennis player.
 

# Table: Championships

# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | year          | int     |
# | Wimbledon     | int     |
# | Fr_open       | int     |
# | US_open       | int     |
# | Au_open       | int     |
# +---------------+---------+
# year is the primary key for this table.
# Each row of this table containts the IDs of the players who won one each tennis tournament of the grand slam.
 

# Write an SQL query to report the number of grand slam tournaments won by each player. Do not include the players who did not win any tournament.

# Return the result table in any order.

# The query result format is in the following example:

 

# Players table:
# +-----------+-------------+
# | player_id | player_name |
# +-----------+-------------+
# | 1         | Nadal       |
# | 2         | Federer     |
# | 3         | Novak       |
# +-----------+-------------+

# Championships table:
# +------+-----------+---------+---------+---------+
# | year | Wimbledon | Fr_open | US_open | Au_open |
# +------+-----------+---------+---------+---------+
# | 2018 | 1         | 1       | 1       | 1       |
# | 2019 | 1         | 1       | 2       | 2       |
# | 2020 | 2         | 1       | 2       | 2       |
# +------+-----------+---------+---------+---------+

# Result table:
# +-----------+-------------+-------------------+
# | player_id | player_name | grand_slams_count |
# +-----------+-------------+-------------------+
# | 2         | Federer     | 5                 |
# | 1         | Nadal       | 7                 |
# +-----------+-------------+-------------------+

# Player 1 (Nadal) won 7 titles: Wimbledon (2018, 2019), Fr_open (2018, 2019, 2020), US_open (2018), and Au_open (2018).
# Player 2 (Federer) won 5 titles: Wimbledon (2020), US_open (2019, 2020), and Au_open (2019, 2020).
# Player 3 (Novak) did not win anything, we did not include them in the result table.


select t.player_id, t.player_name, count(*) as grand_slams_count

from 
(
select p.player_id, p.player_name 
from Players p inner join Championships c
on p.player_id = c.Wimbledon
union all 
select p.player_id, p.player_name
from Players p
join Championships c
on p.player_id = c.Fr_open
union all
select p.player_id, p.player_name
from Players p
join Championships c
on p.player_id = c.US_open
union all
select p.player_id, p.player_name
from Players p
join Championships c
on p.player_id = c.Au_open
) t
group by t.player_id


# Write your MySQL query statement below

with temp_table as 
(
select p.player_id, p.player_name 
from Players p inner join Championships c
on p.player_id = c.Wimbledon
union all 
select p.player_id, p.player_name
from Players p
join Championships c
on p.player_id = c.Fr_open
union all
select p.player_id, p.player_name
from Players p
join Championships c
on p.player_id = c.US_open
union all
select p.player_id, p.player_name
from Players p
join Championships c
on p.player_id = c.Au_open
)


select t.player_id, t.player_name, count(*) as grand_slams_count

from temp_table t
group by t.player_id
