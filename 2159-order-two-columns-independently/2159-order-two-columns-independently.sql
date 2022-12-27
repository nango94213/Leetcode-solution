# Write your MySQL query statement below

with cte as(select *, row_number() over() n from data order by first_col asc),

cte2 as(select *, row_number() over() n from data order by second_col desc)

select t1.first_col, t2.second_col from cte t1 join cte2 t2 on t1.n = t2.n