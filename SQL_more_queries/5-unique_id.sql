-- Task 5: Create table unique_id with unique default id
-- Creates the table unique_id if it does not exist

CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
