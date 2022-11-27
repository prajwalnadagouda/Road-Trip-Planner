import time, threading
import database
import getevents
from flask import Flask, render_template, request
from fuelstations import fetch_fuelstations
from parks import fetch_parks
from amusementparks import fetch_amusement_parks
from flask_cors import CORS
from museums import fetch_museums
from restaurants import fetch_restaurants


app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return 'This Compose/Flask demo has been viewed time(s)'

# @app.route('/updatedatabase')
def update_database():
    print("i am here")
    database.database.update_database()
    threading.Timer(3600, database.database.update_database).start()


@app.route('/getevents',methods=['GET'])
def get_events():
    if request.method == 'GET':
        l1 = request.args.get('l1')
        l2 = request.args.get('l2')
        l3 = request.args.get('l3')
        l4 = request.args.get('l4')
        return getevents.display(l1,l2,l3,l4)
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
    update_database() 
    app.run(host="0.0.0.0", debug=True)
