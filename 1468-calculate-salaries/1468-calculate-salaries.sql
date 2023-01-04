# Write your MySQL query statement below
with cte as(select *, max(salary) over(partition by company_id) best from Salaries)

select company_id, employee_id, employee_name, case when best < 1000 then round(salary, 0) when best <= 10000 then round(salary * 0.76, 0) else round(salary * 0.51, 0) end salary from cte