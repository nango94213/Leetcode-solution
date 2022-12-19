# Write your MySQL query statement below
select c.name from Candidate c join Vote v on c.id = v.candidateId group by c.name order by count(*) desc limit 1
