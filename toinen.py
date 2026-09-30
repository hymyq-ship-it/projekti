
import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="root",
        database="flight_game"
    )
from db import connect_db

db = connect_db()
print("Yhteys toimii!")
db.close()
