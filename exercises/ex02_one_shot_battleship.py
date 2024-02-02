"""EX02 - One Shot Battleship."""

__author__ = "730544766"

"Defining Variables"
grid_size: int = 4
secret_row: int = 3
secret_column: int = 2
blue_box: str = "\U0001F7E6"
red_box: str = "\U0001F7E5"
white_box: str = "\U00002B1C"

"Asks for row and column guesses and makes sure they are in the grid bounds"
row_guess: str = input("Guess a row: ")
while int(row_guess) > grid_size or int(row_guess) < 1:
    row_guess = input(f"The grid is only {grid_size} by {grid_size}. Try again: ")
column_guess: str = input("Guess a column: ")
while int(column_guess) > grid_size or int(column_guess) < 1:
    column_guess = input(f"The grid is only {grid_size} by {grid_size}. Try again: ")

"Checks guess at each coordinate and then loops until grid size is reached."
"If guess matches the secret numbers at the current coordinates then add a red box, if not then add a white box."
"If not either then add a blue box."
row_counter: int = 1
while row_counter <= grid_size:
    column_counter: int = 1
    row_string: str = ""
    while column_counter <= grid_size:
        if int(row_guess) == row_counter and int(column_guess) == column_counter:
            if (int(row_guess) == secret_row and int(column_guess) == secret_column):
                row_string += red_box
            else:
                row_string += white_box
        else:
            row_string += blue_box
        column_counter += 1
    row_counter += 1
    print(row_string)

"Print a message based on if the guess is a hit, in the correct row, in the correct column, or neither."
if int(row_guess) == secret_row and int(column_guess) == secret_column:
    print("Hit!")
else:
    if int(row_guess) == secret_row:
        print("Close! Correct row, wrong column.")
    else:
        if int(column_guess) == secret_column:
            print("Close! Correct column, wrong row.")
        else:
            print("Miss!")