# Write your MySQL query statement below

with cte as(select paid_by, -amount amount from Transactions union all select paid_to, amount from Transactions),

cte2 as(select paid_by user_id, sum(amount) amount from cte group by user_id)

select a.user_id, a.user_name, a.credit+ifnull(b.amount, 0) credit, if(a.credit+ifnull(b.amount, 0) < 0, 'Yes', 'No') credit_limit_breached from Users a left join cte2 b on a.user_id = b.user_id