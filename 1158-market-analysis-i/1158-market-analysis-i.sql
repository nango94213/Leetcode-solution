# Write your MySQL query statement below

 select t.user_id buyer_id, t.join_date, sum(t.info) orders_in_2019 from (select u.user_id, u.join_date,
  CASE
    WHEN year(o.order_date) = 2019 THEN 1
    ELSE 0
  END info from Users u left join Orders o on u.user_id = o.buyer_id) t group by t.user_id order by t.user_id asc