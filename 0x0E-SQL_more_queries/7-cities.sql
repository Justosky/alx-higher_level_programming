-- A script that creates the database hbtn_0d_usa
-- And the table cities (in the database hbtn_0d_usa) MySQL server.

CREATE DATABASE IF NOT EXISTS `htbn_0d_usa`;
CREATE TABLE IF NOT EXISTS `htbn_0d_usa`.`cities`
(
id INT UNIQUE AUTO_INCREMENT NOT NULL,
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
PRIMARY KEY(id),
FOREIGN KEY(state_id) REFERENCES htbn_0d_usa.states(id)
);
