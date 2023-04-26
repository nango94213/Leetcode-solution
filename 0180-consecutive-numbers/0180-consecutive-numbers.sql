# Write your MySQL query statement below

with cte as(select *, lag(num, 1) over() l1, lag(num, 2) over() l2 from Logs)

select distinct num ConsecutiveNums from cte where num = l1 and num = l2 
