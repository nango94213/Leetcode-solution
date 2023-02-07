# Write your MySQL query statement below

select tmp.customer_id, tmp.product_id, p.product_name from (select customer_id, product_id, rank() over(partition by customer_id order by count(product_id) desc) rk  from Orders group by customer_id, product_id) tmp join Products p on tmp.product_id = p.product_id where rk = 1