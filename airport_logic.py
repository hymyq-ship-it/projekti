from db import connect_db

def find_airport_by_name(name):
    db = connect_db()
    cursor = db.cursor()

    # 1. Etsi kaupunki joka alkaa annetulla nimellä
    cursor.execute("""
        SELECT ident, name, municipality, iso_country
        FROM airport
        WHERE municipality LIKE %s
        ORDER BY type DESC
        LIMIT 1
    """, (name + "%",))

    result = cursor.fetchone()

    # 2. Jos ei löytynyt, etsi lentokentän nimi joka alkaa annetulla nimellä
    if result is None:
        cursor.execute("""
            SELECT ident, name, municipality, iso_country
            FROM airport
            WHERE name LIKE %s
            ORDER BY type DESC
            LIMIT 1
        """, (name + "%",))
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
