# Write your MySQL query statement below

select substring(trans_date, 1, 7) AS month, country, count(*) trans_count, sum(
case when state = "approved" then 1 else 0 end) approved_count, sum(amount) trans_total_amount, sum(case when state = "approved" then amount else 0 end) approved_total_amount from Transactions group by month, country