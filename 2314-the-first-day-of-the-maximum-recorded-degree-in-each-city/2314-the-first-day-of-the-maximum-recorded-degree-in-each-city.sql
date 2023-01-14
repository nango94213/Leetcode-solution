# Write your MySQL query statement below

with cte as(select *, rank() over(partition by city_id order by degree desc, day asc) rk from Weather)

select city_id, day, degree from cte where rk = 1