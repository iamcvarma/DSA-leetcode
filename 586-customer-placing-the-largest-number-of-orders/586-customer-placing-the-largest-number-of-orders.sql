# Write your MySQL query statement below
select customer_number from Orders 
group by customer_number
having count(order_number) = (
select count(order_number) cc from Orders group by customer_number
order by cc desc
limit 1
)