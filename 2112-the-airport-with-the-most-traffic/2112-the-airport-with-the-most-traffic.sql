# Write your MySQL query statement below

with cte as(select departure_airport, flights_count from Flights union all select arrival_airport, flights_count from Flights)

select departure_airport airport_id from (select *, rank() over(order by sum(flights_count) desc) ranking from cte group by departure_airport) t where t.ranking = 1