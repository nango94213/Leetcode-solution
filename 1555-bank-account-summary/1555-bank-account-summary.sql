# Write your MySQL query statement below

with cte as(select *, -amount negative from Transactions),

cte2 as(select user_id, credit total from Users union all select paid_by, negative from cte union all select paid_to, amount from cte)

select *, case when credit < 0 then 'Yes' when credit >= 0 then 'No' end credit_limit_breached from (select c.user_id, u.user_name, sum(c.total) credit from cte2 c join Users u on c.user_id = u.user_id group by user_id) gg