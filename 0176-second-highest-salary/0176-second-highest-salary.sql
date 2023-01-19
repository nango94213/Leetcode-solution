# Write your MySQL query statement below

select IFNULL((select max(salary) SecondHighestSalary from (select *, dense_rank() over(order by salary desc) rk from Employee) t where rk = 2 limit 1), NULL) SecondHighestSalary
#select max(salary) SecondHighestSalary from (select *, dense_rank() over(order by salary desc) rk from Employee) t where rk = 2