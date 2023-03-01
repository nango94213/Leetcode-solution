# Write your MySQL query statement below

with cte as(select * from Customer group by customer_id, product_key),

cte2 as(select customer_id, count(*) ct from cte group by customer_id),

cte3 as(select count(*) gt from Product)

select customer_id from cte2, cte3 where ct = gt
