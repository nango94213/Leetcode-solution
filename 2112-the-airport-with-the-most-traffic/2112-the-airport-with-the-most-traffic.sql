# Write your MySQL query statement below

with cte as(select departure_airport, flights_count from Flights union all select arrival_airport, flights_count from Flights)

select departure_airport airport_id from (select *, rank() over(order by total desc) ranking from (select departure_airport, sum(flights_count) total from cte group by departure_airport) t) g where g.ranking = 1