# Write your MySQL query statement below

with cte as(select from_id, to_id, duration from Calls union all select all to_id, from_id, duration from Calls)

select from_id person1, to_id person2, count(*) call_count, sum(duration) total_duration from cte where from_id < to_id group by from_id, to_id