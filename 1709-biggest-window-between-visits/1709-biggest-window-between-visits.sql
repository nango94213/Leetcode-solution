# Write your MySQL query statement below
with cte as(select user_id, '2021-1-1' from UserVisits),

cte2 as(select * from UserVisits union all select * from cte),

cte3 as(select *, lag(visit_date) over(partition by user_id order by visit_date asc) nd from cte2)

select user_id, max(datediff(visit_date, nd)) biggest_window from cte3 group by user_id