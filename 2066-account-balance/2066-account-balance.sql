# Write your MySQL query statement below
with cte as(select *, case when type = 'Deposit' then amount when type = 'Withdraw' then amount * -1 end as net from Transactions)

select account_id, day, sum(net) over(partition by account_id order by day asc) balance from cte