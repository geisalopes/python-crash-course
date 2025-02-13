class MagicCreature:
    """A class to represent a magic creature"""

    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

    def describe_creature(self):
        """Describe the magic creature"""
        print(f"{self.name} lives in {self.habitat}.")


class Dragon(MagicCreature):
    """A class to represent a dragon, a special kind of magic creature."""

    def __init__(self, name, habitat, fire_power):
        """Initialize attributes from the parent class, then add fire power."""
        super().__init__(name, habitat)  # Call the __init__ from the father class
        self.fire_power = fire_power  # Attribute exclusive to the dragon class

    def describe_dragon(self):
        """Describe the dragon."""
        print(
            f"{self.name} live in {self.habitat} and has a fire power of {self.fire_power}."
        )


# Creating a object from the Child class 'Dragon'
smaug = Dragon("Smaug", "Lonely Mountain", 100)

# Calling the methods
smaug.describe_creature()  # Method got from the Father class
smaug.describe_dragon()  # Specific method from the Child class
