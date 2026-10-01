import mysql.connector

def connect_db():
    salasana = input("MYSQL Tietokannan salasana: ")
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password=salasana,
        database="flight_game"
    )
