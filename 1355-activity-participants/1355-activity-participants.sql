# Write your MySQL query statement below
with cte as(select activity, rank() over(order by count(*) asc) r1, rank() over(order by count(*) desc) r2 from Friends group by activity)

select activity from cte where r1 != 1 and r2 != 1