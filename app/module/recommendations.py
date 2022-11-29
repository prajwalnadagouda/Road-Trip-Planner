import random
from flask import jsonify
import mysql.connector as mc


def fetch_recommendations():
    result = {}
    # DB Connection
    connection = mc.connect(host=str("db"), user=str("root"), passwd=str("password123"), database=str("travel"))
    # if DB connection exists
    if connection.is_connected():
        # create cursor
        cursor = connection.cursor(buffered=True)

        cursor.execute("select event_id, event_date, event_performer, event_type, event_venue, latitude, latitude from events")
        events = cursor.fetchall()
        #print(events[0])
        random_events = random.choices(events, k=3)
        random_events = [dict(zip(("event_id", "event_date", "event_performer", "event_type", "event_venue", "latitude", "latitude"), value)) for value in random_events]
        result["events"] = random_events

        cursor.execute("select id, name, latitude, longitude, city, street_address, zip from parks")
        parks = cursor.fetchall()
        #print(parks[0])
        random_parks = random.choices(parks, k=3)
        random_parks = [dict(zip(("id", "name", "latitude", "longitude", "city", "street_address", "zip"), value)) for value in random_parks]
        result["parks"] = random_parks

        cursor.execute("select id, name, latitude, longitude from amusement_parks")
        amusementparks = cursor.fetchall()
        #print(amusementparks[0])
        random_amusementparks = random.choices(amusementparks, k=3)
        random_amusementparks = [dict(zip(("id", "name", "latitude", "longitude"), value)) for value in random_amusementparks]
        result["amusementparks"] = random_amusementparks

        cursor.execute("select id, name, type, latitude, longitude, city, street_address, zip from museums")
        museums = cursor.fetchall()
        #print(museums[0])
        random_museums = random.choices(museums, k=3)
        random_museums = [dict(zip(("id", "name", "type", "latitude", "longitude", "city", "street_address", "zip"), value)) for value in random_museums]
        result["museums"] = random_museums

        cursor.execute("select id, name, category, latitude, longitude, city, street_address, zip from restaurants")
        restaurants = cursor.fetchall()
        #print(restaurants[0])
        random_restaurants = random.choices(restaurants, k=3)
        random_restaurants = [dict(zip(("id", "name", "category", "latitude", "longitude", "city", "street_address", "zip"), value)) for value in random_restaurants]
        result["restaurants"] = random_restaurants

    return jsonify(result)
