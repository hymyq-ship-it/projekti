import math
from airport_logic import get_airport
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

    return pistee


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

    kohde = input("Minne haluat matkustaa?: ").upper()

    jaljella = osta_tiketti(current_ident, kohde)

    if jaljella is None:
        return

    print(f"\n🛫 Nouset koneeseen... Tervemenoa kohteeseen {kohde}!")
    print(f"Pisteitä jäljellä: {jaljella}")


main()
print("\nKiitos pelaamisesta! Toivottavasti nautit pelistä. 😊")
