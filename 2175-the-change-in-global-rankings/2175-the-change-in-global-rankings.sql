# Write your MySQL query statement below
#update points first

with cte as(select team_id, points from TeamPoints union all select team_id, points_change from PointsChange),

cte2 as(select team_id, sum(points) new_points from cte group by team_id),

rank1 as(select *, rank() over(order by points desc, name asc) ranking from TeamPoints),

cte3 as(select t.team_id, t.name, c.new_points from TeamPoints t join cte2 c on t.team_id = c.team_id),

rank2 as(select *, rank() over(order by new_points desc, name asc) ranking from cte3)

select r1.team_id, r1.name, cast(r1.ranking as signed)-cast(r2.ranking as signed) rank_diff from rank1 r1 join rank2 r2 on r1.team_id = r2.team_id