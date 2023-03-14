# Write your MySQL query statement below

select a.user_id buyer_id, a.join_date, count(b.order_id) orders_in_2019 from Users a left join (select * from Orders where year(order_date)=2019) b on a.user_id = b.buyer_id group by a.user_id