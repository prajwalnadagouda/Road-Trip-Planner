import database
import display
from flask import Flask, render_template
from fuelstations import fetch_fuelstations
import time, threading

app = Flask(__name__)

@app.route('/')
def hello():
    return 'This Compose/Flask demo has been viewed time(s)'

# @app.route('/updatedatabase')
def update_database():
    print("i am here")
    threading.Timer(3600, database.database.update_database).start()

@app.route('/display')
def connect_server():
    return display.display()
    return render_template('hello.html', name = "Connected")


@app.route('/fuelstations')
def fetch_fuelstation():
    return fetch_fuelstations(self='')


if __name__ == "__main__":
    update_database()
    app.run(host="0.0.0.0", debug=True)
