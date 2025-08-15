import random as r

# monty hall: monty closes one of the doors that is NOT the zonk
# the monty hall solution states that switching doors gives a greater probability that you get the prize

def assign_prizes_to_doors() -> dict:
    i = r.randint(1, 3) # pick the zonk door
    doors = dict()
    if i == 1:
        doors.update({1: "ZONK"})
        doors.update({2: "LAMBO"})
        doors.update({3: "LAMBO"})
    elif i == 2:
        doors.update({1: "LAMBO"})
        doors.update({2: "ZONK"})
        doors.update({3: "LAMBO"})
    else:
        doors.update({1: "LAMBO"})
        doors.update({2: "LAMBO"})
        doors.update({3: "ZONK"})
    return doors

# monty reveals a non-zonk door (and door player did NOT choose)
def reveal_door(doors: dict, player_door: int) -> int:
    # see which two doors contain lambos
    lambos = []
    for key in doors.keys():
        if doors.get(key) == "LAMBO":
            lambos.append(key)
    shown_door = 0
    if player_door in lambos:
        # get other lambo door that player did not choose
        if lambos[0] != player_door:
            shown_door = lambos[0]
        else:
            shown_door = lambos[1]
    else:
        shown_door = r.choice(lambos)
    print(f'shown door: {shown_door}')
    doors.pop(shown_door)
    return shown_door
# main
print("Welcome to the Monty Hall Show!")
doors = assign_prizes_to_doors()
player_door = int(input("Pick a door from 1 to 3!\n"))
print(f"Amazing, you have picked Door number {player_door}!")
print("I will now reveal one of the doors with a brand new Lamborghini!")
print(f"Door {reveal_door(doors, player_door)} contains a Lambo. *ooh, ahh*\nWill you keep your door, or switch to the other?")
