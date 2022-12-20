# Write your MySQL query statement below
# 
select round(tt.valid*100/tt.total, 2) immediate_percentage from (select count(*) total, sum(t.order_date = t.customer_pref_delivery_date) valid from (select *, rank() over(partition by customer_id order by order_date asc) ranking from Delivery) t where t.ranking = 1) tt