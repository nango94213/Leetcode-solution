# Write your MySQL query statement below

with cte as(select managerID, count(*) counting from Employee group by managerID)

select e.name from cte c join Employee e on e.id = c.managerID where c.counting >= 5