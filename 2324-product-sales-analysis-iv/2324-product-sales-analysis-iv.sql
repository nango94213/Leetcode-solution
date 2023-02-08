# Write your MySQL query statement below

select user_id, product_id from (select a.user_id, a.product_id, rank() over(partition by a.user_id order by sum(a.quantity*b.price) desc) rk from Sales a join Product b on a.product_id = b.product_id group by a.user_id, a.product_id) tmp where tmp.rk = 1