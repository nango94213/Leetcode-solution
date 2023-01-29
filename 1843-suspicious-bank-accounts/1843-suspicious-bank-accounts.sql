# Write your MySQL query statement below

with cte as(select transaction_id, account_id, year(day) y, month(day) m, sum(amount) income from Transactions where type = "Creditor" group by account_id, y, m order by account_id, y, m),

cte2 as(select a.transaction_id, a.account_id, a.y, a.m m1, a.income i1, b.m m2, b.income i2 from cte a join cte b on a.account_id = b.account_id and a.y = b.y and a.m = b.m-1)

select distinct a.account_id from Accounts a join cte2 b on a.account_id = b.account_id where i1 > max_income and i2 > max_income order by transaction_id asc