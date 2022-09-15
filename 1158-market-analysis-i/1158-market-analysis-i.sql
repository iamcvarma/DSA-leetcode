# Write your MySQL query statement below
select user_id as buyer_id,join_date,Count(item_id) as orders_in_2019
from Users U left join Orders O on U.user_id = O.buyer_id AND year(order_date)='2019'
Group By U.user_id