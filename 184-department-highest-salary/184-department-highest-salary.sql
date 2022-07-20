# Write your MySQL query statement below

select m.name Employee, m.salary Salary, g.name Department from Employee m inner join Department g on m.departmentId = g.id where (m.salary, m.departmentId) in (select max(o.salary), o.departmentId from Employee o group by o.departmentId);