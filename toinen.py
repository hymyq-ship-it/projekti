
import mysql.connector

def connect_db():
    salasana = input("MYSQL Tietokannan salasana: ") 
    # koska kaikilla on tämä, niin on helpompaa kysyä salasana kuin vaihtaa kaikkien johonkin tiettyyn...
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password=salasana,
        database="flight_game"
    )
from db import connect_db

db = connect_db()
print("Yhteys toimii!")
db.close()
