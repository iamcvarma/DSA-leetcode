# Write your MySQL query statement below
select name,ifnull(sum(distance),0) as travelled_distance 
from Users U left join Rides R on U.id = R.user_id
Group By U.id
Order BY travelled_distance desc,name