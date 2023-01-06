# Write your MySQL query statement below

with cte as(select * from Customer group by customer_id, product_key having count(*) >= 1),

cte2 as (select customer_id, count(product_key) ct from cte group by customer_id),

cte3 as (select count(*) pct from Product)



#select * from cte order by customer_id
#select * from cte2 order by customer_id
select customer_id from cte2, cte3 where ct = pct