# Write your MySQL query statement below
with cte as(select user_id, s.product_id, quantity, price from Sales s join Product p on s.product_id = p.product_id),

cte2 as(select user_id, product_id, sum(quantity*price) total from cte group by user_id, product_id)

select user_id, product_id from (select user_id, product_id, rank() over(partition by user_id order by total desc) ranking from cte2) t where t.ranking = 1

