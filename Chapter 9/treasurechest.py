class TreasureChest:
    """A simple class to represent a treasure chest."""

    def __init__(self, name, gold, gems):
        self.name = name
        self.gold = gold
        self.gems = gems

    def describe_treasure(self):
        """Display the current state of the treasure chest."""
        print(f"Name: {self.name}, Gold: {self.gold}, Gems: {self.gems}\n")

    def add_gold(self, amount):
        """Increase the amount of gold in the treasure chest."""
        self.gold += amount
        print(f"The gold amount in {self.name} increased to {self.gold}")


# Creating a treasure chest object
treasure = TreasureChest("Ancient Glass", 56, "sapphires")

# Displaying the initial treasure chest information
treasure.describe_treasure()

# Adding more gold to the treasure chest
treasure.add_gold(15)

# Displaying the updated treasure chest information
treasure.describe_treasure()
