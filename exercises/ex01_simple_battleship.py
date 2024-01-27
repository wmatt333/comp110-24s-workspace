"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730544766"
Boat_Location: str = input("Pick a secret boat location between 1 and 4: ")
if int(Boat_Location) > 4:
    print(f"Error! {Boat_Location} too high!")
    exit()
if int(Boat_Location) < 1:
    print(f"Error! {Boat_Location} too low!")
    exit()
Boat_Guess: str = input("Guess a number between 1 and 4: ")
if int(Boat_Guess) > 4:
    print(f"Error! {Boat_Guess} too high!")
    exit()
if int(Boat_Guess) < 1:
    print(f"Error! {Boat_Guess} too low!")
    exit()
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
if int(Boat_Guess) == 1:
    if Boat_Guess == Boat_Location:
        Box1: str = RED_BOX
    if Boat_Guess != Boat_Location:
        Box1 = WHITE_BOX
else:
    Box1 = BLUE_BOX
if int(Boat_Guess) == 2:
    if Boat_Guess == Boat_Location:
        Box2: str = RED_BOX
    if Boat_Guess != Boat_Location:
        Box2 = WHITE_BOX
else:
    Box2 = BLUE_BOX
if int(Boat_Guess) == 3:
    if Boat_Guess == Boat_Location:
        Box3: str = RED_BOX
    if Boat_Guess != Boat_Location:
        Box3 = WHITE_BOX
else:
    Box3 = BLUE_BOX
if int(Boat_Guess) == 4:
    if Boat_Guess == Boat_Location:
        Box4: str = RED_BOX
    if Boat_Guess != Boat_Location:
        Box4 = WHITE_BOX
else:
    Box4 = BLUE_BOX
print(f"{Box1}{Box2}{Box3}{Box4}")
if int(Boat_Location == Boat_Guess):
    print("Correct! You hit the ship.")
else:
    print("Incorrect! You missed the ship.")