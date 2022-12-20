# Write your MySQL query statement below
# 
select round(sum(t.order_date = t.customer_pref_delivery_date)*100/count(*), 2) immediate_percentage from (select *, rank() over(partition by customer_id order by order_date asc) ranking from Delivery) t where t.ranking = 1