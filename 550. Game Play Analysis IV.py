# 550. Game Play Analysis IV
# Medium
# 12535Add to ListShare
# SQL Schema
# Table: Activity
# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | player_id    | int     |
# | device_id    | int     |
# | event_date   | date    |
# | games_played | int     |
# +--------------+---------+
# (player_id, event_date) is the primary key of this table.
# This table shows the activity of players of some game.
# Each row is a record of a player who logged in and played a number of games (possibly 0) before logging out on someday using some device.
 
# Write an SQL query that reports the fraction of players that logged in again on the day after the day they first logged in, rounded to 2 decimal places. In other words, you need to count the number of players that logged in for at least two consecutive days starting from their first login date, then divide that number by the total number of players.
# The query result format is in the following example:
 
# Activity table:
# +-----------+-----------+------------+--------------+
# | player_id | device_id | event_date | games_played |
# +-----------+-----------+------------+--------------+
# | 1         | 2         | 2016-03-01 | 5            |
# | 1         | 2         | 2016-03-02 | 6            |
# | 2         | 3         | 2017-06-25 | 1            |
# | 3         | 1         | 2016-03-02 | 0            |
# | 3         | 4         | 2018-07-03 | 5            |
# +-----------+-----------+------------+--------------+

# Result table:
# +-----------+
# | fraction  |
# +-----------+
# | 0.33      |
# +-----------+
# Only the player with id 1 logged back in after the first day he had logged in so the answer is 1/3 = 0.33



# Write your MySQL query statement below
with tmp_table as
(select player_id, date_add(min(event_date), interval 1 day) as event_date
from Activity
group by player_id)


(select round(count(distinct a.player_id)/ ((select count(distinct a1.player_id) from Activity a1)), 2) 
 as fraction from Activity a
where (a.player_id, a.event_date) in
(select player_id, event_date from tmp_table))


# Write your MySQL query statement below
with lead_date as 
(select player_id, event_date, 
 lead(event_date, 1) over(partition by player_id order by event_date) as lead_date ,
 row_number() over(partition by player_id order by event_date) as log_order
from Activity)

select round(count(distinct t.player_id)/(select count(distinct player_id) from Activity), 2) as fraction from
lead_date t
where datediff(t.lead_date, t.event_date) =1
    and t.lead_date is not null 
    and t.log_order =1

# Write your MySQL query statement below
with lead_date as 
(select player_id, event_date, 
 lead(event_date, 1) over(partition by player_id order by event_date) as lead_date 
from Activity),
total_cnt as (select count(distinct a.player_id) as id_cnt from Activity a),
min_date as (select player_id, min(event_date) as min_time from Activity
             group by player_id)

select round(count(l.player_id)/t.id_cnt, 2) as fraction from 
lead_date l, total_cnt t, min_date m
where datediff(l.lead_date, l.event_date) =1 
and m.min_time = l.event_date
and l.player_id = m.player_id
