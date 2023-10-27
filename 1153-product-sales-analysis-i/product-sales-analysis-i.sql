# Write your MySQL query statement below

SELECT p.product_name,s.year,s.price
FROM Sales as s
inner join Product as p
on s.product_id=p.product_id
order by s.price desc
