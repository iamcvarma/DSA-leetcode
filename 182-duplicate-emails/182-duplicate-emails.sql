# Write your MySQL query statement below
select email as Email 
from Person 
group by Email
having count(id)>1