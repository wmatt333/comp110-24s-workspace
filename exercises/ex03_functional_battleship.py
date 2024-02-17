"""EK03 - Functional Battleship."""

__author__ = "730544766"
import random


# asks user for column and row guess and makes sure it is in bounds
def input_guess(grid_size: int, guess_type: str) -> int:
    """Function 1."""
    assert guess_type == "row" or guess_type == "column"
    guess = int(input(f"Guess a {guess_type}: "))
    while guess > grid_size or guess < 1:
        guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
    return guess


blue_box: str = "\U0001F7E6"
red_box: str = "\U0001F7E5"
white_box: str = "\U00002B1C"


# function that has a while loop that creates and prints boxes based on if the guess is right or wrong
def print_grid(grid_size: int, row_guess: int, column_guess: int, correct: bool) -> None:
    """Function 2."""
    row_counter: int = 1
    while row_counter <= grid_size:
        column_counter: int = 1
        row_string: str = ""
        while column_counter <= grid_size:
            if row_guess == row_counter and column_guess == column_counter:
                if correct is True:
                    row_string += red_box
                else:
                    row_string += white_box
            else:
                row_string += blue_box
            column_counter += 1
        row_counter += 1
        print(row_string)


# function that sees if the player guess matches the secret numbers
def correct_guess(secret_row: int, secret_column: int, row_guess: int, column_guess: int) -> bool:
    """Function 3."""
    if secret_row == row_guess and secret_column == column_guess:
        return True
    else:
        return False
    

# function that combines all of the previous functions to make the whole game work
def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    """Function 4."""
    turns: int = 1
    user_won: bool = False
    while turns <= 5 and user_won is False:
        print(f"=== Turn {turns}/5 ===")
        row_guess: int = input_guess(grid_size, "row")
        column_guess: int = input_guess(grid_size, "column")
        result = correct_guess(secret_row, secret_column, row_guess, column_guess)
        print_grid(grid_size, row_guess, column_guess, result)
        if result is True:
            print(f"Hit! You won in {turns}/5 turns!")
            user_won = True
        else:
            print("Miss!")
            turns += 1
        if turns == 6:
            print("X/5 - Better luck next time!")


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))