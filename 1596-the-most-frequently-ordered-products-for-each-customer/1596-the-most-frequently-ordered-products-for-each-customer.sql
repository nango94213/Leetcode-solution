# Write your MySQL query statement below
with cte as(select c.customer_id, p.product_id, rank() over(partition by customer_id order by count(*) desc) rk, p.product_name from Customers c join Orders o on c.customer_id = o.customer_id join Products p on o.product_id = p.product_id group by c.customer_id, p.product_id)

select customer_id, product_id, product_name from cte where rk = 1