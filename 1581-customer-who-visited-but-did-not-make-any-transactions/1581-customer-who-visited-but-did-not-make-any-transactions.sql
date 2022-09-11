# Write your MySQL query statement below
select customer_id, Count(customer_id) as count_no_trans 
From Visits V Left Join Transactions T on V.visit_id = T.visit_id
Where amount is NULL
Group By customer_id