# Write your MySQL query statement below

with cte as(select *, row_number() over() rw, lead(sold_num) over() gg from Sales)

select sale_date, sold_num - gg diff from cte where rw % 2 = 1