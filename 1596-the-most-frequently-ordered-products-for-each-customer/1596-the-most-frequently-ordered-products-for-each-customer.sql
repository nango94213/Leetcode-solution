# Write your MySQL query statement below
with cte as(select c.customer_id, p.product_id, count(p.product_id) total, p.product_name from Customers c join Orders o on c.customer_id = o.customer_id join Products p on o.product_id = p.product_id group by c.customer_id, p.product_id),

cte2 as(select *, rank() over(partition by customer_id order by total desc) rk from cte)

select customer_id, product_id, product_name from cte2 where rk = 1