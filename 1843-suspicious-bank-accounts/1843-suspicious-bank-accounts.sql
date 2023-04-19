# Write your MySQL query statement below

with cte as(select account_id, year(day) y, month(day) m, sum(if(type="Creditor", amount, 0)) total from Transactions group by account_id, y, m),

cte2 as(select a.account_id, a.m, a.total, b.m m1, b.total t1 from cte a join cte b on a.account_id = b.account_id and a.y = b.y and a.m = b.m+1)

#select * from cte2
select distinct a.account_id from cte2 a join Accounts b on a.account_id = b.account_id where total > max_income and t1 > max_income
