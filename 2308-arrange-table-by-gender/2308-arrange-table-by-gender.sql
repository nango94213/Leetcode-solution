# Write your MySQL query statement below

with cte as(select *, rank() over(partition by gender order by user_id) rk from Genders)

select user_id, gender from cte order by rk, length(gender) desc