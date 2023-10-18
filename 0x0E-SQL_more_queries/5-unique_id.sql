-- unique_id in the current database in your MySQL server.
CREATE table IF NOT EXISTS unique_id(`id` INT UNIQUE DEFAULT 1, `name` VARCHAR(256));
