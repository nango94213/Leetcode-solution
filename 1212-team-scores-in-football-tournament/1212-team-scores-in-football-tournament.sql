# Write your MySQL query statement below

with cte as (select host_team, guest_team, host_goals, guest_goals from Matches union all select guest_team, host_team, guest_goals, host_goals from Matches)

select a.team_id, a.team_name, ifnull(gg.num_points, 0) num_points from Teams a left join (select host_team, sum(case when host_goals > guest_goals then 3 when host_goals = guest_goals then 1 else 0 end) num_points from cte group by host_team) gg on a.team_id = gg.host_team order by num_points desc, team_id asc