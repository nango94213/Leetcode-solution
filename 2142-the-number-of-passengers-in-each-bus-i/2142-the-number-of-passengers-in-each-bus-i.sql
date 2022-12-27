# Write your MySQL query statement below

with cte as(select p.passenger_id, min(b.arrival_time) b_time from Buses b join Passengers p on p.arrival_time <= b.arrival_time group by p.passenger_id)

select b.bus_id, count(c.passenger_id) passengers_cnt from Buses b left join cte c on b.arrival_time = c.b_time group by b.bus_id order by b.bus_id asc