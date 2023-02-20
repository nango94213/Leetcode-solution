# Write your MySQL query statement below

with cte as(select *, rank() over(partition by product_id order by change_date desc) rk from Products where change_date <= date("2019-08-16"))

select distinct a.product_id, ifnull(b.new_price, 10) price from Products a left join (select * from cte where rk = 1) b on a.product_id = b.product_id