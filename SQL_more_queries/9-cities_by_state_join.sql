-- Task 9: List all cities with their corresponding states
-- Lists cities.id, cities.name, and states.name using a JOIN

SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
