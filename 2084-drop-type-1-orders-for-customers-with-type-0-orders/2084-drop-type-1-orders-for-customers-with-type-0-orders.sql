# Write your MySQL query statement below

with cte as(select customer_id mark from Orders where order_type = 0 group by customer_id),

cte2 as (select * from Orders o left join cte c on o.customer_id = c.mark)

select * from(select order_id, customer_id, case when mark is not null and order_type = 1 then null else order_type end order_type from cte2) t where t.order_type is not null