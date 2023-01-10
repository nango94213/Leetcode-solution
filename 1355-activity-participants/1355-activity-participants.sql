# Write your MySQL query statement below
with cte as(select activity, rank() over(order by count(*) desc) rk from Friends group by activity)


select activity from cte, (select max(rk) total from cte) gg where rk != 1 and rk != total
