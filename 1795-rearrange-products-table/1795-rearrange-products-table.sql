# Write your MySQL query statement below
select product_id, "store1" as store, store1 as price from Products Where store1 is not NULL
UNION
select product_id, "store2" as store, store2 as price from Products Where store2 is not NULL
UNION
select product_id, "store3" as store, store3 as price from Products Where store3 is not NULL