# Write your MySQL query statement below
select user_id, count(follower_id) as followers_count 
from Followers
Group By user_id
Order By user_id