# Write your MySQL query statement below

with cte as(select *, count(salary) ct from Employees group by salary),

cte2 as(select salary from cte where ct != 1)

select *, dense_rank() over(order by salary) team_id from Employees where salary in (select * from cte2)