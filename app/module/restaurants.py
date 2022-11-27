import mysql.connector as mc
import pandas as pd

# Data source: https://www.kaggle.com/datasets/khushishahh/fast-food-restaurants-across-us
# Fast_Food_Restaurants_US_CA.csv

def fetch_restaurants():

    # Read and filter museums with state as California
    restaurants = pd.read_csv("Fast_Food_Restaurants_US_CA.csv")
    #print(restaurants)

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
        for i, restaurant in restaurants.iterrows():
            try:
                # id, name, categories, latitude, longitude, address, city, postalCode
                id = restaurant["id"]
                name = restaurant["name"]
                category = restaurant["categories"]
                latitude = restaurant["latitude"]
                longitude = restaurant["longitude"]
                street_address = restaurant["address"]
                city = restaurant["city"]
                zip = restaurant["postalCode"]

                # id, name, type, latitude, longitude, street_address, city, zip
                cursor.execute("insert into restaurants VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                              (id, name, category, latitude, longitude, city, street_address, zip))
            except mc.Error as err:
                print
                print("Something went wrong: {}".format(err))
            # Commit, close cursor and connection
        connection.commit()
        cursor.close()
        connection.close()
    return "Success."
