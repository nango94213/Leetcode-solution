# Write your MySQL query statement below

with cte as (select product_id, year(purchase_date) yy, count(*) total from Orders group by product_id, yy having total >= 3)

select distinct(a.product_id) from cte a join cte b on a.product_id = b.product_id and a.yy = b.yy - 1