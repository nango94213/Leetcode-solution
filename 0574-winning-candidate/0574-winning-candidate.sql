# Write your MySQL query statement below

select a.name from Candidate a join (select candidateId, rank() over(order by count(*) desc) rk from vote group by candidateId) b on a.id = b.candidateId where rk = 1
