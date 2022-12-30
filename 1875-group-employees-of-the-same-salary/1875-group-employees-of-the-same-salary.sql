# Write your MySQL query statement below

with cte as(select *, count(salary) over(partition by salary) ct from Employees)


select employee_id, name, salary, dense_rank() over(order by salary) team_id from cte where ct >= 2