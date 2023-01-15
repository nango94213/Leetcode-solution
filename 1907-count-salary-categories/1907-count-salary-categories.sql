# Write your MySQL query statement below

with cte as(select *, case when income < 20000 then "Low Salary" when income <= 50000 then "Average Salary" when income > 50000 then "High Salary" end category from Accounts)

select tmp.category, count(c.category) accounts_count from (select "Low Salary" category union select "Average Salary" union select "High Salary") tmp left join cte c on tmp.category = c.category group by tmp.category