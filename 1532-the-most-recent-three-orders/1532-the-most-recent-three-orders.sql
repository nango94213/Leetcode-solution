# Write your MySQL query statement below
with cte as(select c.customer_id, c.name, o.order_id, o.order_date, rank() over(partition by c.customer_id order by order_date desc) rk from Customers c join Orders o on c.customer_id = o.customer_id order by c.name asc, c.customer_id asc, o.order_date desc)

select name customer_name, customer_id, order_id, order_date from cte where rk <= 3