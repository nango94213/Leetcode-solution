# Write your MySQL query statement below

with cte as(select * from Calls union all select to_id, from_id, duration from Calls),

cte2 as(select * from cte where from_id < to_id)

select from_id person1, to_id person2, count(duration) call_count, sum(duration) total_duration from cte2 group by from_id, to_id