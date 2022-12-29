# Write your MySQL query statement below

with cte as(select *, rank() over(partition by gender order by user_id asc) ranking from Genders)

select user_id, gender from cte order by ranking asc, length(gender) desc