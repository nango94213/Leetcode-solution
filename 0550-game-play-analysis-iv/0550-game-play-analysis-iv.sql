# Write your MySQL query statement below

with cte as(select *, min(event_date) over(partition by player_id) fd from Activity)


select round(ct/total, 2) fraction from (select count(distinct player_id) ct from cte where event_date = DATE_ADD(fd, INTERVAL 1 DAY)) a, (select count(distinct player_id) total from Activity) b
