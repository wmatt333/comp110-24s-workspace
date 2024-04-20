"""File to define Fish class."""


class Fish:
    """Creates an object that represents a fish."""

    age: int

    def __init__(self):
        """Sets the fish's age to 0."""
        self.age = 0
        return None
    
    def one_day(self):
        """Represents one day for the fish."""
        self.age += 1
        return None