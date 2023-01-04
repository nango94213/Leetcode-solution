# Write your MySQL query statement below

with cte as(select b.apple_count a , b.orange_count b , c.apple_count c , c.orange_count d from Boxes b left join Chests c on b.chest_id = c.chest_id)

select sum(a) apple_count, sum(b) orange_count from (select a, b from cte union all select c, d from cte) gg