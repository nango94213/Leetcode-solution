# Write your MySQL query statement below

with cte as(select p.product_name, p.product_id, o.order_id, o.order_date, rank() over(partition by p.product_name, p.product_id order by o.order_date desc) rk from Products p join Orders o on p.product_id = o.product_id)

select product_name, product_id, order_id, order_date from cte where rk = 1 order by product_name asc, product_id asc, order_id asc