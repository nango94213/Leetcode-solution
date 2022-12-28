# Write your MySQL query statement below
with cte as(select *, case when weekday(submit_date) < 5 then 1 else null end weekend_cnt, case when weekday(submit_date) >= 5 then 1 else null end working_cnt from Tasks)

select count(weekend_cnt) weekend_cnt, count(working_cnt) working_cnt from cte