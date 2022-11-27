import requests
import json
import mysql.connector as mc


def fetch_fuelstations(self):
    api_key = "0aiWJnXwZc8Idclk8fTtvcrUugETNV8xlwy8yzHT"

    # fuel_types=all&status_code=E&access_code=public&restricted_access=false&state=CA
    response = requests.get(
        "https://developer.nrel.gov/api/alt-fuel-stations/v1.json?"
        + "fuel_type=all&status_code=E&access_code=public&restricted_access=false&state=CA&api_key="
        + api_key)

    fuelstations = json.loads(response.text)['fuel_stations']

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
        cursor = connection.cursor(buffered = True)

        # Loop and store fuelstations
        for fuelstation in fuelstations:
            id = fuelstation["id"]
            fuel_type_code = fuelstation["fuel_type_code"]
            station_name = fuelstation["station_name"]
            latitude = fuelstation["latitude"]
            longitude = fuelstation["longitude"]
            facility_type = fuelstation["facility_type"]
            access_days_time = fuelstation["access_days_time"]
            city = fuelstation["city"]
            street_address = fuelstation["street_address"]
            zip = fuelstation["zip"]
            try:
                # id, fuel_type_code, station_name, latitude, longitude, facility_type, access_days_time, city, street_address, zip
                cursor.execute("insert into fuelstations VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (id, fuel_type_code, station_name, latitude, longitude, facility_type, access_days_time, city, street_address, zip))
            except mc.Error as err:
                pass
        # Commit, close cursor and connection
        connection.commit()
        cursor.close()
        connection.close()
    return "Success."
