# Write your MySQL query statement below
select actor_id,director_id 
from ActorDirector 
Group By actor_id,director_id
having count(director_id)>=3