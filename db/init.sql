CREATE DATABASE travel;

use travel;

CREATE TABLE events (event_id INT PRIMARY KEY, event_date DATE, event_type VARCHAR(255), event_venue VARCHAR(255), event_lat FLOAT(10, 6),event_lon FLOAT(10, 6), event_lowest_price INT, event_highest_price INT);

CREATE TABLE fuelstations (id INT PRIMARY KEY, fuel_type_code VARCHAR(30), station_name VARCHAR(100), latitude FLOAT(10, 6), longitude FLOAT(10,6), facility_type VARCHAR(30), access_days_time VARCHAR(255), city VARCHAR(100), street_address VARCHAR(100), zip VARCHAR(10));

CREATE TABLE parks(id VARCHAR(40) PRIMARY KEY, park_code VARCHAR(30), name VARCHAR(50), latitude FLOAT(10,6), longitude FLOAT(10, 6), description VARCHAR(500), city VARCHAR(100), street_address VARCHAR(100), zip VARCHAR(10));
