# 1341. Movie Rating
# Medium
# 6332Add to ListShare
# SQL Schema
# Table: Movies
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | movie_id      | int     |
# | title         | varchar |
# +---------------+---------+
# movie_id is the primary key for this table.
# title is the name of the movie.
# Table: Users
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | user_id       | int     |
# | name          | varchar |
# +---------------+---------+
# user_id is the primary key for this table.
# Table: Movie_Rating
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | movie_id      | int     |
# | user_id       | int     |
# | rating        | int     |
# | created_at    | date    |
# +---------------+---------+
# (movie_id, user_id) is the primary key for this table.
# This table contains the rating of a movie by a user in their review.
# created_at is the user's review date. 
 
# Write the following SQL query:
# •	Find the name of the user who has rated the greatest number of movies.
# In case of a tie, return lexicographically smaller user name.
# •	Find the movie name with the highest average rating in February 2020.
# In case of a tie, return lexicographically smaller movie name.
# The query is returned in 2 rows, the query result format is in the following example:
# Movies table:
# +-------------+--------------+
# | movie_id    |  title       |
# +-------------+--------------+
# | 1           | Avengers     |
# | 2           | Frozen 2     |
# | 3           | Joker        |
# +-------------+--------------+

# Users table:
# +-------------+--------------+
# | user_id     |  name        |
# +-------------+--------------+
# | 1           | Daniel       |
# | 2           | Monica       |
# | 3           | Maria        |
# | 4           | James        |
# +-------------+--------------+

# Movie_Rating table:
# +-------------+--------------+--------------+-------------+
# | movie_id    | user_id      | rating       | created_at  |
# +-------------+--------------+--------------+-------------+
# | 1           | 1            | 3            | 2020-01-12  |
# | 1           | 2            | 4            | 2020-02-11  |
# | 1           | 3            | 2            | 2020-02-12  |
# | 1           | 4            | 1            | 2020-01-01  |
# | 2           | 1            | 5            | 2020-02-17  | 
# | 2           | 2            | 2            | 2020-02-01  | 
# | 2           | 3            | 2            | 2020-03-01  |
# | 3           | 1            | 3            | 2020-02-22  | 
# | 3           | 2            | 4            | 2020-02-25  | 
# +-------------+--------------+--------------+-------------+

# Result table:
# +--------------+
# | results      |
# +--------------+
# | Daniel       |
# | Frozen 2     |
# +--------------+

# Daniel and Monica have rated 3 movies ("Avengers", "Frozen 2" and "Joker") but Daniel is smaller lexicographically.
# Frozen 2 and Joker have a rating average of 3.5 in February but Frozen 2 is smaller lexicographically.


# # Write your MySQL query statement below
(select t1.Name as results from 
(
select u.Name, m.user_id, count(m.movie_id) as cnt
from Users u join Movie_Rating m
on u.user_id = m.user_id
group by m.user_id 
order by cnt desc, u.Name
limit 1) t1
 )

union

(
select t.title as results from
(
select mo.title, mr.movie_id, avg(mr.rating) as avg_rate from Movies mo join Movie_Rating mr
on mo.movie_id = mr.movie_id
where date_format(mr.created_at, '%Y-%m') = '2020-02' 
group by mr.movie_id 
order by avg_rate desc, mo.title 
limit 1 ) t
)
