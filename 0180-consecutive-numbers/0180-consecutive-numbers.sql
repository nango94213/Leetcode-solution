# Write your MySQL query statement below

with cte as(select *, lead(num, 1) over() l1, lead(num, 2) over() l2 from Logs)

select distinct(num) ConsecutiveNums from cte where num = l1 and l1 = l2