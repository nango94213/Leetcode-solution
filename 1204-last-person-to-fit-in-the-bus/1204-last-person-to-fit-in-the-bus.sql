# Write your MySQL query statement below
with cte as(select *, sum(weight) over(order by turn) total from Queue),

cte2 as(select *, lead(total) over() ld from cte)

select person_name from cte2 where total <= 1000 and (ld is null or ld >  1000)
