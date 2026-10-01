#1. Haen lentokentän koordinaatit


from db import connect_db

def get_airport(ident):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("""
        SELECT ident, name, latitude_deg, longitude_deg 
        FROM airport 
        WHERE ident = %s
    """, (ident,))
    result = cursor.fetchone()
    cursor.close()
    db.close()
    return result
