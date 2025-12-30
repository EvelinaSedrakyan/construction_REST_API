CREATE DATABASE construction_db;
CREATE USER construction_user WITH PASSWORD 'construction_pass';
ALTER DATABASE construction_db OWNER TO construction_user;
GRANT ALL PRIVILEGES ON DATABASE construction_db TO construction_user;
