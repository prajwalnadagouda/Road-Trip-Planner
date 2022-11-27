import database
import display
from flask import Flask, render_template
from fuelstations import fetch_fuelstations
from parks import fetch_parks
from amusementparks import fetch_amusement_parks
from museums import fetch_museums
from restaurants import fetch_restaurants


app = Flask(__name__)

@app.route('/')
def hello():
    return 'This Compose/Flask demo has been viewed time(s)'

@app.route('/updatedatabase')
def update_database():
    return database.database.update_database()
    return render_template('hello.html')

@app.route('/display')
def connect_server():
    return display.display()

    return render_template('hello.html', name = "Connected")


@app.route('/fuelstations')
def fetch_fuelstation():
    return fetch_fuelstations(self='')


@app.route('/parks')
def get_parks():
    return fetch_parks()


@app.route('/amusementparks')
def get_amusement_parks():
    return fetch_amusement_parks()


@app.route('/museums')
def get_museums():
    return fetch_museums()


@app.route('/restaurants')
def get_restaurants():
    return fetch_restaurants()



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
