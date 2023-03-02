# Write your MySQL query statement below


with cte as(select managerId from Employee group by managerId having count(*) >= 5)


select a.name from Employee a join cte b on a.id = b.managerId