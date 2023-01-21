# Write your MySQL query statement below

with cte as(select *, rank() over(partition by department_id order by mark desc) rk, count(student_id) over(partition by department_id) total from Students)

select student_id, department_id, ifnull(round((rk-1) * 100 / (total-1), 2), 0) percentage from cte