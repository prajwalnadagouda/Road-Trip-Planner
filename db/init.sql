CREATE DATABASE travel;

use travel;

CREATE TABLE events (event_id INT PRIMARY KEY, event_date DATE, event_venue VARCHAR(255), event_lat FLOAT(10, 6),event_lon FLOAT(10, 6), event_lowest_price INT, event_highest_price INT);

