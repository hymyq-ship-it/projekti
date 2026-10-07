import math
import random
from time import sleep

from airport_logic import find_airport_by_name, get_airport
from distance import haversine
from puzzle import puzzles

ODOTUS = 1


def ratkaise_pulmat(maara, lisakysymykset=False):
    pisteet = 0
    kysymykset = random.sample(puzzles, maara)

    for p in kysymykset:
        vastaus = input(f"\n🧩 {p['kysymys']} ").strip().lower()
        if vastaus == p["vastaus"].lower():
            print("✅ Oikein! +1 piste")
            pisteet += 1
        else:
            print(f"❌ Väärin! Oikea vastaus: {p['vastaus']}")

    if lisakysymykset and pisteet > 0:
        jatkaa = input("Haluatko vielä jatkaa kysymyksien kanssa? (joo/ei): ").lower()
        if jatkaa == "joo":
            pisteet += ratkaise_pulmat(1, True)

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
    kerrottu = False

    while pisteet < hinta:
        print(f"\n💰 Tarvitset vielä {hinta - pisteet} pistettä.")
        if not kerrottu:
            print("Ratkaise pulmia ansaitaksesi pisteitä!")
            kerrottu = True

        pisteet += ratkaise_pulmat(1, pisteet + 1 >= hinta)

    print(f"\n🎫 Hei! Olet kerännyt tarpeeksi pisteitä ({pisteet}).")
    print("Pääset lentokoneeseen!")
    return pisteet - hinta


def main():

    current_ident = "EFHK"  # Helsinki-Vantaa

    kohde_syote = input("Minne haluat matkustaa? ").strip()

    # ICAO-koodi (4 kirjainta)
    if len(kohde_syote) == 4 and kohde_syote.isalpha():
        kohde = kohde_syote.upper()
    else:
        airport = find_airport_by_name(kohde_syote)
        if airport is None:
            print("❌ Kohdetta ei löytynyt. Kokeile toista kaupunkia tai ICAO-koodia.")
            return
        kohde = airport[0]
        print(f"➡️ Matkustat lentokentälle: {airport[1]} ({kohde})")

    jaljella = osta_tiketti(current_ident, kohde)

    if jaljella is None:
        return

    print(f"\n🛫 Nouset koneeseen... Tervemenoa kohteeseen {kohde}!")
    print(f"Pisteitä jäljellä: {jaljella}")


print("✈️ Tervetuloa lentopeliin!")
sleep(ODOTUS)
while True:
    if main() == None:
        continue
    vastaus = input("\nHaluatko explore ja matkustaa muihin maihin? (k/e): ").lower()
    if vastaus != "k":
        print("\nKiitos pelaamisesta! Toivottavasti nautit pelistä. 😊")
        break
