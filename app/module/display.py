from flask import jsonify
import mysql.connector as mc
from mysql.connector import errorcode

user= "root"#parser.get('dblogin_detail', 'username')
password= "password123"#parser.get('dblogin_detail', 'password')
database= "travel" #parser.get('dblogin_detail', 'database')
host= "db" #parser.get('dblogin_detail', 'host')
def display():
    try:
        mydb = mc.connect(host="db", user="root", passwd="password123", database="travel")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            return("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            return("Database does not exist")
        else:
            return(str(err))
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM events")
    myresult = mycursor.fetchall()
    return jsonify(myresult)