# Write your MySQL query statement below
select name,IF(sum(distance) is Null,0,sum(distance)) as travelled_distance 
from Users U left join Rides R on U.id = R.user_id
Group By U.id
Order BY travelled_distance desc,name