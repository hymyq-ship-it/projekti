

def min():
    print("Tervetuloa lentopelille")
    aloitta=float(input("Haluatko alotta pelamaan? joo/ei:"))
    if aloitta =="joo":
        start_game()
    else:
        print("Heippa")

def start_game():
    import random
    print("peli alkaa...")
    current_airport = "Helsinki-Vantaan"
    print(f" olet {current_airport} lentokentä nyt. sinun matka on alkanyt ja  ")
    

import random

#Pulmakysymykset: lista sanakirjoja (kysymys, vastaus)
puzzles = [
    {"kysymys": "Mikä on Suomen pääkaupunki?", "vastaus": "helsinki"},
    {"kysymys": "Paljonko on 9 * 9?", "vastaus": "81"},
    {"kysymys": "Mikä on veden kemiallinen kaava?", "vastaus": "h2o"},
    {"kysymys": "Kuinka monta päivää viikossa on?", "vastaus": "7"},
    {"kysymys": "Mikä planeetta tunnetaan punaisena planeettana?", "vastaus": "mars"},
    {"kysymys": "Paljonko on 100 / 4?", "vastaus": "25"},
    {"kysymys": "Mikä eläin sanoo 'miau'?", "vastaus": "kissa"},
    {"kysymys": "Mikä on Suomen kansalliseläin?", "vastaus": "karhu"},
    {"kysymys": "Kuinka monta jalkaa hämähäkillä on?", "vastaus": "8"},
    {"kysymys": "Mikä on vuoden ensimmäinen kuukausi?", "vastaus": "tammikuu"},

    {"kysymys": "Paljonko on 12 + 15?", "vastaus": "27"},
    {"kysymys": "Mikä on maailman suurin valtameri?", "vastaus": "tyynimeri"},
    {"kysymys": "Mikä väri syntyy, kun sininen ja keltainen sekoitetaan?", "vastaus": "vihreä"},
    {"kysymys": "Kuinka monta tuntia vuorokaudessa on?", "vastaus": "24"},
    {"kysymys": "Mikä eläin tunnetaan ihmisen parhaana ystävänä?", "vastaus": "koira"},
    {"kysymys": "Paljonko on 15 - 7?", "vastaus": "8"},
    {"kysymys": "Mikä on Ruotsin pääkaupunki?", "vastaus": "tukholma"},
    {"kysymys": "Kuinka monta vuodenaikaa Suomessa on?", "vastaus": "4"},
    {"kysymys": "Mikä planeetta on lähimpänä Aurinkoa?", "vastaus": "merkurius"},
    {"kysymys": "Paljonko on 6 * 7?", "vastaus": "42"},

    {"kysymys": "Mikä on Norjan pääkaupunki?", "vastaus": "oslo"},
    {"kysymys": "Kuinka monta minuuttia tunnissa on?", "vastaus": "60"},
    {"kysymys": "Mikä on Suomen kansalliskukka?", "vastaus": "kielo"},
    {"kysymys": "Paljonko on 50 + 25?", "vastaus": "75"},
    {"kysymys": "Mikä eläin on maailman suurin maalla elävä eläin?", "vastaus": "norsu"},
    {"kysymys": "Mikä on Japanin pääkaupunki?", "vastaus": "tokio"},
    {"kysymys": "Kuinka monta kirjainta suomenkielisessä sanassa 'lentokone' on?", "vastaus": "9"},
    {"kysymys": "Paljonko on 144 / 12?", "vastaus": "12"},
    {"kysymys": "Mikä kaasu on tärkein osa Maan ilmakehästä?", "vastaus": "typpi"},
    {"kysymys": "Mikä eläin munii mutta on nisäkäs?", "vastaus": "vesinokkaeläin"},

    {"kysymys": "Mikä on Ranskan pääkaupunki?", "vastaus": "parisi"},
    {"kysymys": "Paljonko on 11 * 11?", "vastaus": "121"},
    {"kysymys": "Kuinka monta mannerta maapallolla on?", "vastaus": "7"},
    {"kysymys": "Mikä on Australian pääkaupunki?", "vastaus": "canberra"},
    {"kysymys": "Mikä eläin on tunnettu mustavalkoisista raidoistaan?", "vastaus": "seepra"},
    {"kysymys": "Paljonko on 90 - 37?", "vastaus": "53"},
    {"kysymys": "Mikä on Italian pääkaupunki?", "vastaus": "rooma"},
    {"kysymys": "Kuinka monta sekuntia minuutissa on?", "vastaus": "60"},
    {"kysymys": "Mikä planeetta tunnetaan renkaistaan?", "vastaus": "saturnus"},
    {"kysymys": "Mikä on Espanjan pääkaupunki?", "vastaus": "madrid"},

    {"kysymys": "Paljonko on 13 + 29?", "vastaus": "42"},
    {"kysymys": "Mikä on Saksan pääkaupunki?", "vastaus": "berliini"},
    {"kysymys": "Kuinka monta sormea ihmisellä yleensä on?", "vastaus": "10"},
    {"kysymys": "Mikä eläin tunnetaan viidakon kuninkaana?", "vastaus": "leijona"},
    {"kysymys": "Paljonko on 8 * 8?", "vastaus": "64"},
    {"kysymys": "Mikä on Islannin pääkaupunki?", "vastaus": "reykjavik"},
    {"kysymys": "Mikä on kovin luonnossa esiintyvä mineraali?", "vastaus": "timantti"},
    {"kysymys": "Kuinka monta päivää karkausvuodessa on?", "vastaus": "366"},
    {"kysymys": "Paljonko on 200 / 10?", "vastaus": "20"},
    {"kysymys": "Mikä on Tanskan pääkaupunki?", "vastaus": "kööpenhamina"},

    {"kysymys": "Mikä on Yhdysvaltojen pääkaupunki?", "vastaus": "washington"},
    {"kysymys": "Paljonko on 17 + 18?", "vastaus": "35"},
    {"kysymys": "Mikä eläin tuottaa villaa?", "vastaus": "lammas"},
    {"kysymys": "Mikä on Kanadan pääkaupunki?", "vastaus": "ottawa"},
    {"kysymys": "Kuinka monta kylkiluuta ihmisellä yleensä on?", "vastaus": "24"},
    {"kysymys": "Paljonko on 7 * 7?", "vastaus": "49"},
    {"kysymys": "Mikä on Kreikan pääkaupunki?", "vastaus": "ateena"},
    {"kysymys": "Mikä on maailman suurin eläin?", "vastaus": "sinivalas"},
    {"kysymys": "Paljonko on 81 / 9?", "vastaus": "9"},
    {"kysymys": "Mikä on Portugalin pääkaupunki?", "vastaus": "lisboa"},

    {"kysymys": "Mikä väri syntyy punaisen ja valkoisen sekoituksesta?", "vastaus": "vaaleanpunainen"},
    {"kysymys": "Paljonko on 14 * 3?", "vastaus": "42"},
    {"kysymys": "Mikä on Brasilian pääkaupunki?", "vastaus": "brasilia"},
    {"kysymys": "Kuinka monta pyörää tavallisessa polkupyörässä on?", "vastaus": "2"},
    {"kysymys": "Mikä eläin tunnetaan pitkästä kaulastaan?", "vastaus": "kirahvi"},
    {"kysymys": "Paljonko on 75 - 25?", "vastaus": "50"},
    {"kysymys": "Mikä on Viron pääkaupunki?", "vastaus": "tallinna"},
    {"kysymys": "Mikä on aurinkokuntamme suurin planeetta?", "vastaus": "jupiter"},
    {"kysymys": "Kuinka monta jalkaa hämähäkillä on? ", "vastaus": "8"},
    {"kysymys": "Paljonko on 5 * 12?", "vastaus": "60"},

    {"kysymys": "Mikä on Sveitsin pääkaupunki?", "vastaus": "bern"},
    {"kysymys": "Mikä eläin pystyy vaihtamaan väriä ympäristön mukaan?", "vastaus": "kameleontti"},
    {"kysymys": "Paljonko on 64 / 8?", "vastaus": "8"},
    {"kysymys": "Kuinka monta kirjainta sanassa 'lentokenttä' on?", "vastaus": "11"},
    {"kysymys": "Mikä on Belgian pääkaupunki?", "vastaus": "bryssel"},
    {"kysymys": "Mikä planeetta on tunnettu sinisestä väristään?", "vastaus": "neptunus"},
    {"kysymys": "Paljonko on 19 + 21?", "vastaus": "40"},
    {"kysymys": "Mikä on Egyptin pääkaupunki?", "vastaus": "kairo"},
    {"kysymys": "Kuinka monta kuukautta vuodessa on?", "vastaus": "12"},
    {"kysymys": "Mikä eläin tunnetaan hitaasta liikkumisestaan?", "vastaus": "laiskiainen"},

    {"kysymys": "Paljonko on 1000 - 1?", "vastaus": "999"},
    {"kysymys": "Mikä on Puolan pääkaupunki?", "vastaus": "varsova"},
    {"kysymys": "Mikä on ihmisen suurin elin?", "vastaus": "iho"},
    {"kysymys": "Paljonko on 16 * 5?", "vastaus": "80"},
    {"kysymys": "Mikä on Kiinan pääkaupunki?", "vastaus": "peking"},
    {"kysymys": "Kuinka monta hammasta aikuisella ihmisellä yleensä on?", "vastaus": "32"},
    {"kysymys": "Mikä eläin tunnetaan siitä, että se rakentaa patoja?", "vastaus": "majava"},
    {"kysymys": "Paljonko on 120 / 6?", "vastaus": "20"},
    {"kysymys": "Mikä on Etelä-Korean pääkaupunki?", "vastaus": "seoul"},
    {"kysymys": "Mikä on maailman korkein vuori?", "vastaus": "everest"},

    {"kysymys": "Paljonko on 23 + 17?", "vastaus": "40"},
    {"kysymys": "Mikä on Irlannin pääkaupunki?", "vastaus": "dublin"},
    {"kysymys": "Mikä eläin tunnetaan mustavalkoisena ja syö bambua?", "vastaus": "panda"},
    {"kysymys": "Kuinka monta päivää normaalissa vuodessa on?", "vastaus": "365"},
    {"kysymys": "Paljonko on 9 * 6?", "vastaus": "54"},
    {"kysymys": "Mikä on Itävallan pääkaupunki?", "vastaus": "wien"},
    {"kysymys": "Mikä on maailman suurin aavikko?", "vastaus": "antarktis"},
    {"kysymys": "Paljonko on 45 / 5?", "vastaus": "9"},
    {"kysymys": "Mikä on Uuden-Seelannin pääkaupunki?", "vastaus": "wellington"},
    {"kysymys": "Mikä eläin on tunnettu siitä, että se nukkuu talviunta?", "vastaus": "karhu"},
]

def ratkaise_pulmat(maara):
     pisteet=0
     kysymykset = random.sample(puzzles, maara)  
     
    # satunnainen valinta
     for p in kysymykset:
        vastaus = input(f"\n🧩 {p['kysymys']} ").strip().lower() 
        if vastaus == p["vastaus"]: 
            print("✅ Oikein! +1 piste") 
            pisteet += 1 
        else:
            print(f"❌ Väärin! Oikea vastaus: {p['vastaus']}")
        return pisteet

def osta_tiketti(hinta):
    pisteet = 0 
    while pisteet < hinta:
        print(f"\n💰 Tiketti maksaa {hinta} pistettä. Sinulla on {pisteet}.")
        print("Ratkaise pulmia ansaitaksesi pisteitä!") 
        pisteet += ratkaise_pulmat(1)
        print(f"\n🎫 Tiketti ostettu! ({pisteet} pistettä käytetty)")
        return pisteet - hinta  
    # ylijäävät pisteet säilyvät

#Pääsilmukka
print("✈️ Tervetuloa lentopeliin!") 
kohde = input("Minne haluat matkustaa? ") 
jaljella = osta_tiketti(hinta=3) 
print(f"\n🛫 Nouset koneeseen... Tervemenoa kohteeseen {kohde}!") 
print(f"Pisteitä jäljellä: {jaljella}")
