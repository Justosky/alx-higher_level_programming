-- A script that creates the database hbtn_0d_usa
-- And the table cities (in the database hbtn_0d_usa) MySQL server.

CREATE DATABASE IF NOT EXIST `htbn_0d_usa`;
CREATE TABLE IF NOT EXISTS `htbn_0d_usa`.`cities`
(
id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
state_id INT NOT NULL FOREIGN KEY REFERENCES `states`.`id`
);
