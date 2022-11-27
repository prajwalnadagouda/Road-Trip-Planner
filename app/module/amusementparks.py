import requests
import json
import mysql.connector as mc

#https://queue-times.com/en-US/parks.json


def fetch_amusement_parks():
    response = requests.get("https://queue-times.com/en-US/parks.json")
    data = json.loads(response.text)
    # Filter amusement parks with country as United States and timezone as America/Los_Angeles
    amusement_parks = [j for i in data for j in i["parks"] if j["timezone"] == "America/Los_Angeles" and j["country"] == "United States"]
    #print(amusement_parks)
    # DB Connection
    connection = mc.connect(
        host=str("db"),
        user=str("root"),
        passwd=str("password123"),
        database=str("travel")
    )
    # if DB connection exists
    if connection.is_connected():
        # create cursor
        cursor = connection.cursor(buffered=True)

        # Loop and store parks
        for park in amusement_parks:
            try:
                # id, name, latitude, longitude
                id = park["id"]
                name = park["name"]
                latitude = park["latitude"]
                longitude = park["longitude"]
                cursor.execute("insert into amusement_parks VALUES (%s,%s,%s,%s)",
                               (id, name, latitude, longitude))
            except mc.Error as err:
                pass
            # Commit, close cursor and connection
        connection.commit()
        cursor.close()
        connection.close()
    return "Success."


