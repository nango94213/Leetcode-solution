# Write your MySQL query statement below

with cte as(select *, DATE_ADD(purchase_date, INTERVAL 7 DAY) d2 from Purchases)

select a.user_id from Purchases a join cte b on a.user_id = b.user_id and a.purchase_id != b.purchase_id and a.purchase_date >= b.purchase_date and a.purchase_date <= b.d2 group by a.user_id order by a.user_id

#select * from cte