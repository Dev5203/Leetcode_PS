# Write your MySQL query statement below
select w.name,w.population,w.area
FROM WORLD as w
where w.population>=25000000 or w.area>=3000000