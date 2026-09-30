

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
    {"kysymys": "Mikä lentää ilman siipiä?", "vastaus": "aika"},
    {"kysymys": "Paljonko on 7 * 8?", "vastaus": "56"},
     {"kysymys": "Mikä maa alkaa kirjaimella S ja siellä on Eiffel-torni? (vihje: ei ala S:llä!)", "vastaus": "ranska"},
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
