"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730544766"
boat_location: str = input("Pick a secret boat location between 1 and 4: ")
if int(boat_location) > 4:
    print(f"Error! {boat_location} too high!")
    exit()
if int(boat_location) < 1:
    print(f"Error! {boat_location} too low!")
    exit()
boat_guess: str = input("Guess a number between 1 and 4: ")
if int(boat_guess) > 4:
    print(f"Error! {boat_guess} too high!")
    exit()
if int(boat_guess) < 1:
    print(f"Error! {boat_guess} too low!")
    exit()
blue_box: str = "\U0001F7E6"
red_box: str = "\U0001F7E5"
white_box: str = "\U00002B1C"
if int(boat_guess) == 1:
    if boat_guess == boat_location:
        box1: str = red_box
    if boat_guess != boat_location:
        box1 = white_box
else:
    box1 = blue_box
if int(boat_guess) == 2:
    if boat_guess == boat_location:
        box2: str = red_box
    if boat_guess != boat_location:
        box2 = white_box
else:
    box2 = blue_box
if int(boat_guess) == 3:
    if boat_guess == boat_location:
        box3: str = red_box
    if boat_guess != boat_location:
        box3 = white_box
else:
    box3 = blue_box
if int(boat_guess) == 4:
    if boat_guess == boat_location:
        box4: str = red_box
    if boat_guess != boat_location:
        box4 = white_box
else:
    box4 = blue_box
print(f"{box1}{box2}{box3}{box4}")
if int(boat_location == boat_guess):
    print("Correct! You hit the ship.")
else:
    print("Incorrect! You missed the ship.")