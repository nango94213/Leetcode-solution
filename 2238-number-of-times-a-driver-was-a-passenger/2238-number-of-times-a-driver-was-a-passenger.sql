# Write your MySQL query statement below

with cte as(select distinct(driver_id) dd from Rides)
select dd driver_id, count(passenger_id) cnt from cte left join Rides on dd = passenger_id group by dd

