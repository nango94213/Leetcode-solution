# Write your MySQL query statement below

with cte as(select *, rank() over(partition by product_id order by change_date desc) rk from Products where change_date <= '2019-08-16'),

cte2 as(select * from cte where rk = 1),

cte3 as(select distinct(product_id) from Products)

select p1.product_id, if (p2.product_id is null, 10, p2.new_price) price from cte3 p1 left join cte2 p2 on p1.product_id = p2.product_id