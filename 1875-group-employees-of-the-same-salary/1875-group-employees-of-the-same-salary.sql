# Write your MySQL query statement below

with cte as(select salary from Employees group by salary having count(name) >= 2)

select a.employee_id, a.name, a.salary, dense_rank() over(order by salary asc) team_id from Employees a join cte b on a.salary = b.salary