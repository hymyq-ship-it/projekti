def min():
    print("Tervetuloa lentopelille")
    aloitta=float(input("Haluatko alotta pelamaan? joo/ei:"))
    if aloitta =="joo":
        start_game()
    else:
        print("Heippa")

def start_game():
    print("peli alkaa...")
    print(f" olet {current_airport} lentokentä nyt. sinun matka on alkanyt ja  ")

min()
current_airport = get_first_airport_id()
