# Write your MySQL query statement below

with cte as(select Wimbledon counting from Championships  union all select Fr_open from Championships union all select US_open from Championships Union all select Au_open from Championships),

cte2 as(select player_id, player_name, count(player_id) grand_slams_count from Players p join cte c on p.player_id = c.counting group by player_name order by grand_slams_count asc)

select * from cte2