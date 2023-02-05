# Write your MySQL query statement below

with cte as(select *, row_number() over() rn from Logs)

select min(log_id) start_id, max(log_id) end_id from cte group by log_id - rn order by start_id