# Write your MySQL query statement below
SELECT p.firstname , p.lastname,a.city,a.state
FROM PERSON as p 
left join Address as a
ON p.personID=a.personID