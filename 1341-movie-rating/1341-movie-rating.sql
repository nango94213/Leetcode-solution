# Write your MySQL query statement below

with cte as(select name from (select a.user_id, b.name, rank() over(order by count(*) desc, b.name) rk from MovieRating a join Users b on a.user_id = b.user_id group by a.user_id) tmp where rk = 1),

cte2 as(select title from (select a.movie_id, b.title, rank() over(order by avg(rating) desc, b.title) rk from MovieRating a join Movies b on a.movie_id = b.movie_id where created_at between '2020-02-01' and '2020-02-28' group by a.movie_id) tmp where rk = 1)

select name results from cte union select title from cte2 