class Wizard:
    """A class to represent a wizard."""

    def __init__(self, name, power_level):
        self.name = name
        self.power_level = power_level

    def describe_wizard(self):
        """Describe a wizard"""
        print(f"{self.name} has {self.power_level} of power level.")

    def increase_power_level(self, amount):
        self.power_level += amount
        print(f"The power level from {self.name} was increased to {self.power_level}.")


class DarkWizard(Wizard):
    """A class to represent a different type of wizard."""

    def __init__(self, name, power_level, dark_power):
        """Initialize attributes from the parent class, then add dark_power."""
        super().__init__(name, power_level)  # Call the __init__ from the father class
        self.dark_power = dark_power  # Attribute exclusive to the dark wizard class

    def describe_dark_wizard(self):
        """Describe the dark wizard."""
        print(
            f"{self.name} has {self.power_level} of power level and his dark power is {self.dark_power}."
        )

    def use_dark_power(self):
        print(
            f"⚡️{self.name} unleashes the dark power of {self.dark_power}! The air trembles with dark energy!"
        )


# Creating a object from the Child class 'Dark Wizard'
saruman = DarkWizard("Saruman", 200, "Storms")

# Calling the methods
saruman.describe_wizard()  # Method got from the Father class
saruman.increase_power_level(100)
saruman.describe_dark_wizard()  # Specific method from the Child class
saruman.use_dark_power()
