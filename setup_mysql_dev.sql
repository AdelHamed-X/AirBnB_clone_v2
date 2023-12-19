-- This script prepares a MySQL server for the HBNB clone project

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost'
    IDENTIFIED WITH authentication_plugin BY 'hbnb_dev_pwd';
GRANT * ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';