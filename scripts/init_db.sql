DROP DATABASE IF EXISTS construction_db;
DROP ROLE IF EXISTS construction_user;

CREATE USER construction_user
WITH PASSWORD 'construction_password';

CREATE DATABASE construction_db
    OWNER = construction_user
    ENCODING = 'UTF8';

GRANT ALL PRIVILEGES ON DATABASE construction_db TO construction_user;
