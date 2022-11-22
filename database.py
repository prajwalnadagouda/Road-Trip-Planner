import requests
import json
from datetime import datetime

class database:
    server_connection=0
    peers_assigned=0
    p=0

    def update_database(self): 
        events = requests.get('https://api.seatgeek.com/2/events?per_page=10&venue.state=CA&client_id=MzAxNTQ4MTV8MTY2NzY4MzY2Ni41NjMyMjg4')
        events= json.loads(events.text)['events']
        for event in events:
            event_id = event['id']
            event_date = event['datetime_utc']
            event_date = datetime.strptime(event_date,'%Y-%m-%dT%H:%M:%S')
            event_venue = event["venue"]["name_v2"]
            event_lon = event["venue"]["location"]["lon"]
            event_lat = event["venue"]["location"]["lat"]
            event_highest_price = event['stats']['highest_price']
            event_lowest_price = event['stats']['lowest_price']
            print(event_id, datetime.strptime(event_date,'%Y-%m-%dT%H:%M:%S'), event_venue, event_lat ,event_lon, event_lowest_price, event_highest_price)
            # print(event['datetime_utc'])
            # print(event["venue"]["location"]["lon"])
            # print(event["venue"]["location"]["lat"])
            # print(event['stats']['lowest_price'])
            # print(event['stats']['lowest_price'])
            # print(event['stats']['highest_price'])
        print("wassup")
        return "asas"
        

p= database()
p.update_database()