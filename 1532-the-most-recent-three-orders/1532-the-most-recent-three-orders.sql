# Write your MySQL query statement below
with cte as(select c.customer_id, c.name, o.order_id, o.order_date, rank() over(partition by c.customer_id order by order_date desc) rk from Customers c join Orders o on c.customer_id = o.customer_id)

select name customer_name, customer_id, order_id, order_date from cte where rk in (1, 2, 3) order by name asc, customer_id asc, order_date desc