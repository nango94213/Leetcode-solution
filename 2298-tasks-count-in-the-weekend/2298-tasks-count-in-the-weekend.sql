# Write your MySQL query statement below

select sum(weekday(submit_date)<5) weekend_cnt, sum(weekday(submit_date)>=5) working_cnt from Tasks