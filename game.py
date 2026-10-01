import math
from airport_logic import get_airport,get_maanosat,get_maat
from distance import haversine
from puzzle import puzzles
import random

def ratkaise_pulmat(maara):
    pisteet = 0
    kysymykset = random.sample(puzzles, maara)

    for p in kysymykset:
        vastaus = input(f"\n🧩 {p['kysymys']} ").strip().lower()
        if vastaus == p["vastaus"].lower():
            print("✅ Oikein! +1 piste")
            pisteet += 1
        else:
            print(f"❌ Väärin! Oikea vastaus: {p['vastaus']}")

    return pisteet


def laske_tarvittavat_pisteet(current_ident, target_ident):
    current = get_airport(current_ident)
    target = get_airport(target_ident)

    if target is None:
        print("❌ Lentokenttää ei löytynyt. Tarkista ICAO-koodi.")
        return None

    lat1, lon1 = current[2], current[3]
    lat2, lon2 = target[2], target[3]

    distance = haversine(lat1, lon1, lat2, lon2)
    needed_points = math.ceil(distance / 1000)

    print(f"\n✈️ Matka {current[1]} -> {target[1]} on {distance:.0f} km")
    print(f"Tarvitset {needed_points} pistettä päästäksesi perille.\n")

    return needed_points


def osta_tiketti(current_ident, target_ident):
    hinta = laske_tarvittavat_pisteet(current_ident, target_ident)

    if hinta is None:
        return None

    pisteet = 0

    while pisteet < hinta:
        print(f"\n💰 Tarvitset {hinta} pistettä. Sinulla on {pisteet}.")
        print("Ratkaise pulmia ansaitaksesi pisteitä!")
        pisteet += ratkaise_pulmat(1)

    print(f"\n🎫 Hei! Olet kerännyt tarpeeksi pisteitä ({pisteet}).")
    print("Pääset lentokoneeseen!")
    return pisteet - hinta


def main():
    print("✈️ Tervetuloa lentopeliin!")

    current_ident = "EFHK"  # Helsinki-Vantaa
    continent = str(maanosa())
    maa(continent)
    #kohde = input("Anna kohteen ICAO-koodi (esim. EGLL, KJFK): ").upper()

    jaljella = osta_tiketti(current_ident, kohde)

    if jaljella is None:
        return

    print(f"\n🛫 Nouset koneeseen... Tervemenoa kohteeseen {kohde}!")
    print(f"Pisteitä jäljellä: {jaljella}")

maanosatermit = {
    "EU": "Eurooppa",
    "SA": "Etelä-Amerikka",
    "NA": "Pohjois-Amerikka",
    "AF": "Afrikka",
    "AN": "Antarktika",
    "AS": "Aasia",
    "OC": "Oseania"
}

def maanosa():
    print()
    maanosat = get_maanosat()
    num = -1
    for i in maanosat:
        num+=1
        print(f"{num}: {maanosatermit[i[0]]}") # maanosa / continent
    annum = "EU" # default
    while True:
        try:
            kohde = int(input("Anna maanosan numero: "))
            if kohde < 0:
                print("Anna oikean maanosan numero.")
                continue
            elif kohde > len(maanosat):
                print("Anna oikean maanosan numero.")
                continue
            annum = maanosat[int(kohde)][0]
            break
        except:
            print("Anna numero.")
    print(annum)
    return annum

def maa(continent): # default on EU
    print()
    maat_maanosassa = get_maat(maanosa=continent)
    num = -1
    for i in maat_maanosassa:
        num+=1
        print(f"{num}: {i[1]}")
    annum = maat_maanosassa[0][0] # default
    while True:
        try:
            kohde = int(input("Anna maan numero: "))
            if kohde < 0:
                print("Anna oikean maan numero.")
                continue
            elif kohde > len(maat_maanosassa):
                print("Anna oikean maan numero.")
                continue
            annum = maat_maanosassa[int(kohde)][0]
            break
        except:
            print("Anna numero.")
    print(annum)
    return annum


main()
print("\nKiitos pelaamisesta! Toivottavasti nautit pelistä. 😊")
