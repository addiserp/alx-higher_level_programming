-- a script that creates database and table to the MySQL server user user_0d_1.
CREATE database IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE table IF NOT EXISTS cities(`id` INT NOT NULL AUTO_INCREMENT UNIQUE  PRIMARY KEY,
state_id INT,FOREIGN KEY(state_id) REFERENCES states(id) , `name` VARCHAR(256) NOT NULL);
