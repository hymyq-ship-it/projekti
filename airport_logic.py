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

def get_maanosat():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("""
    SELECT continent FROM country GROUP BY continent ORDER BY continent ASC
    """)
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result

def get_maat(maanosa="EU"):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute(f"""
    SELECT iso_country,name FROM country WHERE continent = '{maanosa}' ORDER BY name ASC
    """)
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result

def get_lentokentat(maa="FI"):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute(f"""
    SELECT iso_country,name,ident,type,municipality FROM airport WHERE iso_country = '{maa}' ORDER BY type,name
    """)
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result