from db import connect_db

def find_airport_by_name(name):
    db = connect_db()
    cursor = db.cursor()

    cursor.execute("""
        SELECT ident, name, municipality, iso_country
        FROM airport
        WHERE municipality LIKE %s OR name LIKE %s
        LIMIT 1
    """, (f"%{name}%", f"%{name}%"))

    result = cursor.fetchone()
    cursor.close()
    db.close()
    return result


def get_airport(ident):
    db = connect_db()
    cursor = db.cursor()

    cursor.execute("""
        SELECT ident, name, latitude_deg, longitude_deg
        FROM airport
        WHERE ident = %s
        LIMIT 1
    """, (ident,))

    result = cursor.fetchone()
    cursor.close()
    db.close()
    return result
