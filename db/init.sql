CREATE DATABASE travel;

use travel;

CREATE TABLE events (event_id INT PRIMARY KEY, event_date DATE, event_venue VARCHAR(255), event_lat INT,event_lon INT, event_lowest_price INT, event_highest_price INT);

