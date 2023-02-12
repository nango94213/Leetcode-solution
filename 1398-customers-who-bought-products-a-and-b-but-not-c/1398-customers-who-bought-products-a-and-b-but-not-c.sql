# Write your MySQL query statement below

select a.customer_id, a.customer_name from Customers a join Orders b on a.customer_id = b.customer_id group by a.customer_id having sum(product_name="A") > 0 and sum(product_name='B') > 0 and sum(product_name='C') = 0