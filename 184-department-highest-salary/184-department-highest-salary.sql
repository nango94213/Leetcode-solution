# Write your MySQL query statement below

select m.name Employee, m.salary Salary, g.name Department from Employee m inner join Department g on m.departmentId = g.id where m.salary = (select max(a.salary) from Employee a inner join Department b on a.departmentId = b.id group by b.name having b.name = g.name);