# Write your MySQL query statement below

with cte as(select *, rank() over(partition by date(day) order by amount desc) rk from Transactions)

select transaction_id from cte where rk = 1 order by transaction_id asc