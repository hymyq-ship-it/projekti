import mysql.connector
salasana = ""
def connect_db():
    global salasana
    if salasana == "": # kysyy vain kerran
        salasana = input("MYSQL Tietokannan salasana: ")
    try:

        return mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password=salasana,
            database="flight_game"
        )
    except:
        print("Jotain meni pieleen...")
        salasana = ""
        return connect_db()
