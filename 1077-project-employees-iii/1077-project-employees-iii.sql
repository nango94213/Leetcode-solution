# Write your MySQL query statement below

select project_id, employee_id from (select p.project_id, e.employee_id, rank() over(partition by p.project_id order by experience_years desc) rk from Project p join Employee e on p.employee_id = e.employee_id) tmp where rk = 1