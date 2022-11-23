import database
import display
from flask import Flask, render_template
from fuelstations import fetch_fuelstations

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
