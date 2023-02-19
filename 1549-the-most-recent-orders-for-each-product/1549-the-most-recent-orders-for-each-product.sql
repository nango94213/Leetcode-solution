# Write your MySQL query statement below

select product_name, product_id, order_id, order_date from (select b.product_name, b.product_id, a.order_id, a.order_date, rank() over(partition by b.product_id order by a.order_date desc) rk from Orders a join Products b on a.product_id = b.product_id) t where t.rk = 1 order by product_name, product_id, order_id