# Write your MySQL query statement below

with cte as(select user_id, '2021-1-1' from UserVisits group by user_id),

cte2 as(select * from UserVisits cte union select * from cte),

cte3 as(select *, lag(visit_date) over(partition by user_id order by visit_date asc) pp from cte2)

select user_id, max(datediff(visit_date, pp)) biggest_window from cte3 group by user_id