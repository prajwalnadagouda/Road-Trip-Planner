import mysql.connector as mc
import pandas as pd

# Data source: museums_ca.csv

def fetch_museums():

    # Read and filter museums with state as California
    museums = pd.read_csv("museums_ca.csv")
    #print(museums)

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
        for i, museum in museums.iterrows():
            try:
                # Museum ID, Museum Name, Museum Type, Latitude, Longitude, Street Address (Physical Location), City (Physical Location), Zip Code (Physical Location)
                id = museum["Museum ID"]
                name = museum["Museum Name"]
                type = museum["Museum Type"]
                latitude = museum["Latitude"]
                longitude = museum["Longitude"]
                street_address = museum["Street Address (Physical Location)"]
                city = museum["City (Physical Location)"]
                zip = museum["Zip Code (Physical Location)"]

                # id, name, type, latitude, longitude, street_address, city, zip
                cursor.execute("insert into museums VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                              (id, name, type, latitude, longitude, street_address, city, zip))
            except mc.Error as err:
                print
                print("Something went wrong: {}".format(err))
            # Commit, close cursor and connection
        connection.commit()
        cursor.close()
        connection.close()
    return "Success."
