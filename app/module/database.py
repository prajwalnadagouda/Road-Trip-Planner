from flask import jsonify
import configparser
import json
import requests
from datetime import datetime
import mysql.connector as mc


class database:
    def update_database():
        user= "root"
        password= "password123"
        database= "travel"
        host= "db"
        events = requests.get('https://api.seatgeek.com/2/events?per_page=50&venue.state=CA&client_id=MzAxNTQ4MTV8MTY2NzY4MzY2Ni41NjMyMjg4')
        events= json.loads(events.text)['events']
        mydb = mc.connect(
        host=str(host),
        user=str(user),
        passwd=str(password),
        database=str(database)
        )
        mycursor = mydb.cursor(buffered=True)
        for event in events:
            event_id = event['id']
            event_performer = event["performers"][0]["name"]
            event_type = event["performers"][0]["taxonomies"][0]["name"]
            event_date = event['datetime_utc']
            event_date = datetime.strptime(event_date,'%Y-%m-%dT%H:%M:%S')
            event_venue = event["venue"]["name_v2"]
            event_lon = event["venue"]["location"]["lon"]
            event_lat = event["venue"]["location"]["lat"]
            event_highest_price = event['stats']['highest_price']
            event_lowest_price = event['stats']['lowest_price']
            # print(event_id, event_date, event_venue, event_lat ,event_lon, event_lowest_price, event_highest_price)
            try:
                mycursor.execute("insert into events VALUES (%s,%s, %s, %s, %s,%s,%s,%s,%s)",(event_id, event_date, event_performer, event_type, event_venue, event_lat ,event_lon, event_lowest_price, event_highest_price))
            except:
                pass
        mydb.commit()
        mydb.close()
        

p= database()