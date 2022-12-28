# Write your MySQL query statement below

select count(case when weekday(submit_date)<5 then 1 else null end) weekend_cnt, count(case when weekday(submit_date)>=5 then 1 else null end) working_cnt from Tasks