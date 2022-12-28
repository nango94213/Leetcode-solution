# Write your MySQL query statement below

with cte as(select customer_id, min(order_type) order_type from Orders group by customer_id)

select * from Orders where (customer_id, order_type) in (select * from cte)