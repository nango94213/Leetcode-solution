# Write your MySQL query statement below

with cte as(select count(distinct player_id) total from Activity),

cte2 as(select *, min(event_date) over(partition by player_id) gg from Activity)

select ifnull(round(count(a.player_id) / b.total, 2), 0.00) fraction from cte2 a, cte b where a.event_date = DATE_ADD(a.gg, INTERVAL 1 DAY)


