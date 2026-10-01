import math
from airport_logic import get_airport,get_maanosat,get_maat,get_lentokentat
from distance import haversine
from puzzle import puzzles
import random
from time import sleep
from db import connect_db

def ratkaise_pulmat(maara,lisakysymykset):
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
            pisteet+=ratkaise_pulmat(1,True)
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
    print(f"Matkaan tarvitsee {needed_points} pistettä.\n")

    return needed_points


def osta_tiketti(current_ident, target_ident):
    hinta = laske_tarvittavat_pisteet(current_ident, target_ident)

    if hinta is None:
        return None

    pisteet = 0
    kerrottu = False
    while pisteet < hinta:

        print(f"\n💰 Tarvitset vielä {hinta-pisteet} pistettä.")
        if kerrottu == False: # jotta se ei sano tätä joka kerta, uskotaan että käyttäjä tietää jo.
            print("Ratkaise pulmia ansaitaksesi pisteitä!")
        kerrottu=True
        pisteet += ratkaise_pulmat(1, pisteet+1 >= hinta)

    print(f"\n🎫 Hei! Olet kerännyt tarpeeksi pisteitä ({pisteet}).")
    print("Pääset lentokoneeseen!")
    return pisteet - hinta

odotus = 1

def main():
    print("✈️ Tervetuloa lentopeliin!")
    sleep(odotus)
    print("Aloitat Helsinki-Vantaalta. Pääset valitsemaan paikan mihin haluat lentää. Ensimmäisenä kysymme tietokoneellasi olevan tietokannan salasanaa.")
    sleep(odotus)
    connect_db().close() # jotta se ei kysyisi myöhemmin
    current_ident = "EFHK"  # Helsinki-Vantaa
    for i in range(10): #kymmenen lentokenttää, voi muokkaa vaikka yhteen jos haluaa...
        continent = "EU"
        if i == 9:
            print("Koska tämä on viimeinen etappi, valitsemme aloituspaikan puolestasi eli matkaamme takaisin Helsinki-Vantaalle.")
        if i < 9:
            continent = str(maanosa())
        country = "FI"
        if i < 9: 
            country = maa(continent)
        kohde = current_ident
        if i < 9:
            kohde = lentokentta(country)
        airport = get_airport(kohde)
        sleep(odotus)

        jaljella = osta_tiketti(current_ident, kohde)

        if jaljella is None:
            return

        print(f"\n🛫 Nouset koneeseen... Tervemenoa kohteeseen {airport[1]}!")
        print(f"Pisteitä jäljellä: {jaljella}")
        sleep(1)
        print()
        sleep(1)
        print()
        sleep(1)
        if i < 9:
            print(f"Olet {airport[1]}. Mihin haluat seuraavaksi mennä?")
        else:
            print("Olipa hieno matka.")
            print()
            sleep(1)

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
    sleep(odotus)
    print()
    print("Maanosat:")
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
    print(f"Valitsit: {annum}")
    return annum

def maa(continent):
    sleep(odotus)
    print()
    print("Maat:")
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
    print(f"Valitsit: {annum}")
    return annum

def lentokentta(country):
    sleep(odotus)
    print()
    print("Lentokentät:")
    lentokentat = get_lentokentat(maa=country)
    num = -1
    for i in lentokentat:
        num+=1
        # formaatissa: 67: nimi (ICAO / type / kunta (jos on))
        print(f"{num}: {i[1]} ({i[2]} / {i[3]} / {i[4]})")
    annum = lentokentat[0][2] # default
    while True:
        try:
            kohde = int(input("Anna lentokentän numero: "))
            if kohde < 0:
                print("Anna oikean lentokentän numero.")
                continue
            elif kohde > len(lentokentat):
                print("Anna oikean lentokentän numero.")
                continue
            annum = lentokentat[int(kohde)][2]
            break
        except:
            print("Anna numero.")
    print(f"Valitsit: {annum}")
    return annum


main()
print("\nKiitos pelaamisesta! Toivottavasti nautit pelistä. 😊")
