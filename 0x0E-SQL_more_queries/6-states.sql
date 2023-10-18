-- a script that creates database and table to the MySQL server user user_0d_1.
CREATE database IF NOT EXISTS hbtn_0d_usa;
CREATE table IF NOT EXISTS states(`id` INT UNIQUE  NOT NULL PRIMARY KEY, `name` VARCHAR(256) NOT NULL);
