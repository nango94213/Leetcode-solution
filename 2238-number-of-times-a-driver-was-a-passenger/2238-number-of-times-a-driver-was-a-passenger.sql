# Write your MySQL query statement below

with cte as(select passenger_id, count(*) ct from Rides group by passenger_id)

select distinct driver_id, ifnull(ct, 0) cnt from Rides a left join cte b on a.driver_id = b.passenger_id