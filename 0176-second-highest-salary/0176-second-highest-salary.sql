# Write your MySQL query statement below

select max(salary) SecondHighestSalary from (select *, dense_rank() over(order by salary desc) rk from Employee) t where rk = 2