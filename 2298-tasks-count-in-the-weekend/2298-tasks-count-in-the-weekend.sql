# Write your MySQL query statement below

select sum(if(WEEKDAY(submit_date)>4, 1, 0)) weekend_cnt, sum(if(WEEKDAY(submit_date)<=4, 1, 0)) working_cnt from Tasks