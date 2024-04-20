"""File to define Bear class."""


class Bear:
    """Creates an object that represents a bear."""

    age: int
    hunger_score: int

    def __init__(self):
        """Sets the bear's age and hunger."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Represents one day for the bear."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int) -> None:
        """Increases the bear's hunger from eating."""
        self.hunger_score += num_fish
        return None