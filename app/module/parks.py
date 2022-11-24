import requests
import json
import mysql.connector as mc

# https://www.nps.gov/subjects/developer/get-started.htm
# 93rP5HcQmidnex1cj9YWeFD8MhenmPJBc3vEdKVz

def fetch_parks():
    api_key = "93rP5HcQmidnex1cj9YWeFD8MhenmPJBc3vEdKVz"

    response = requests.get("https://developer.nps.gov/api/v1/parks?stateCode=ca&limit=2000&api_key=" + api_key)
    parks = json.loads(response.text)['data']

    # DB Connection
    connection = mc.connect(
        host=str("127.0.0.1"),
        port=33000,
        user=str("root"),
        passwd=str("password123"),
        database=str("travel")
    )
    # if DB connection exists
    if connection.is_connected():
        # create cursor
        cursor = connection.cursor(buffered=True)

        # Loop and store parks
        for park in parks:
            try:
                pass
                # id, parkCode, fullName, latitude, longitude, description, city, streetAddress, zip
                id = park["id"]
                park_code = park["parkCode"]
                name = park["fullName"]
                latitude = park["latitude"]
                longitude = park["longitude"]
                description = park["description"][:500]
                addresses = park["addresses"]
                address = list(filter(lambda item: item['type'] == 'Physical', addresses))[0]
                city = address["city"]
                zip = address["postalCode"]
                street_address = ' '.join(str(x) for x in {k: v for k, v in address.items() if k.startswith('line')}.values())

                #print(id + ", " + park_code + ", " + name + ", " + latitude + ", " + longitude + ", " + description + ", " + city + ", " + street_address + ", " + zip)

                cursor.execute("insert into parks VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                               (id, park_code, name, latitude, longitude, description, city, street_address, zip))
            except mc.Error as err:
                print("Something went wrong: {}".format(err))
            # Commit, close cursor and connection
        connection.commit()
        cursor.close()
        connection.close()
    return "Success."


