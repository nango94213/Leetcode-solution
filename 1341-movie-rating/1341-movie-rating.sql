# Write your MySQL query statement below

with cte as(select u.user_id, u.name, rank() over(order by count(*) desc, u.name asc) rk from Users u join MovieRating m on u.user_id = m.user_id group by u.user_id),

cte2 as(select m.title, rank() over(order by avg(r.rating) desc, m.title asc) rk from Movies m join MovieRating r on m.movie_id = r.movie_id where r.created_at between '2020-02-01' and '2020-02-28' group by m.title)



select name results from cte where rk = 1 union select title from cte2 where rk = 1