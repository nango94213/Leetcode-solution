# Write your MySQL query statement below

with cte as (select home_team_id, away_team_id, home_team_goals, away_team_goals from Matches union all select away_team_id, home_team_id, away_team_goals, home_team_goals from Matches)

select a.team_name, gg.matches_played matches_played, gg.points points, gg.goal_for goal_for, gg.goal_against goal_against, gg.goal_diff goal_diff from Teams a join (select home_team_id, sum(case when home_team_goals > away_team_goals then 3 when home_team_goals = away_team_goals then 1 else 0 end) points, count(*) matches_played, sum(home_team_goals) goal_for, sum(away_team_goals) goal_against, sum(home_team_goals) - sum(away_team_goals) goal_diff from cte group by home_team_id) gg on a.team_id = gg.home_team_id order by points desc, goal_diff desc, team_name asc