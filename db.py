import mysql.connector
import toinen
def get_first_airport_id():
    db = toinen.connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT id FROM airport ORDER BY id LIMIT 1")
    result = cursor.fetchone()
    cursor.close()
    db.close()
    return result[0]
