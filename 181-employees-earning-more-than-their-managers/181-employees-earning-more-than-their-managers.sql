# Write your MySQL query statement below
select e.name Employee from Employee e where e.salary > (select s.salary from Employee s where s.id = e.managerId);