# Write your MySQL query statement below
with cte as(select visited_on, sum(amount) total from Customer group by visited_on order by visited_on asc)

#select * from cte
select visited_on, sum(total) over(order by visited_on asc ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) amount,round(avg(total) over(order by visited_on asc ROWS BETWEEN 6 PRECEDING AND CURRENT ROW), 2) average_amount from cte limit 100 offset 6
