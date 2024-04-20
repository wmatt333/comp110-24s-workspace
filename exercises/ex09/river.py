"""File to define River class!"""


__author__ = "730544766"


from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """Represents the ecosystem for the bears and fish."""

    day: int
    fish: list[Fish]
    bears: list[Bear] 

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Gets rid of fish and bears that are too old."""
        new_fish: list[Fish] = []
        new_bears: list[Bear] = []
        for bear in self.bears:
            if bear.age <= 5:
                new_bears.append(bear)
        for fish in self.fish:
            if fish.age <= 3:
                new_fish.append(fish)
        self.bears = new_bears
        self.fish = new_fish
        return None

    def bears_eating(self):
        """Removes fish that the bears eat and gives bears that much hunger."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None
    
    def check_hunger(self):
        """Gets rid of bears that starved!"""
        new_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                new_bears.append(bear)
        self.bears = new_bears
        return None
        
    def repopulate_fish(self):
        """Increases the amount of fish depending on how many there already are."""
        amount: int = (len(self.fish) // 2) * 4
        i: int = 0
        while i < amount:
            self.fish.append(Fish)
            i += 1
        return None
    
    def repopulate_bears(self):
        """Increases the amount of bears depending on how many there already are."""
        amount: int = len(self.bears) // 2
        i: int = 0
        while i < amount:
            self.bears.append(Bear)
            i += 1
        return None

    def remove_fish(self, amount: int) -> None:
        """Removes fish from the start of the list."""
        start: int = amount
        total: int = len(self.fish)
        new_fish: list[Fish] = []
        while start < total:
            new_fish.append(self.fish[start])
            start += 1
        self.fish = new_fish
        return None

    def view_river(self) -> None:
        """Prints out the day and number of fish and bears."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Runs the one day function 7 times to represent a week."""
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        return None