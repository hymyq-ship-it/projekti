import mysql.connector
salasana = ""
def connect_db():
    if salasana == "": # kysyy vain kerran
        salasana = input("MYSQL Tietokannan salasana: ")
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password=salasana,
        database="flight_game"
    )
