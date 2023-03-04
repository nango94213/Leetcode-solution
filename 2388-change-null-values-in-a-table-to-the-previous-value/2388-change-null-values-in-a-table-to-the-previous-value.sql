# Write your MySQL query statement below

with cte as(select *, row_number() over() rn from CoffeeShop),

cte2 as(select *, count(drink) over(order by rn) gg from cte)

select id, first_value(drink)  over(partition by gg) drink from cte2