# Write your MySQL query statement below

with cte as(select user_id, round(sum(action = 'confirmed')/count(time_stamp), 2) confirmation_rate from Confirmations group by user_id)

select a.user_id, ifnull(b.confirmation_rate, 0) confirmation_rate from Signups a left join cte b on a.user_id = b.user_id
