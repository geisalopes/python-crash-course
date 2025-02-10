class Wizard:
    """A simple class to represent a wizar."""

    def __init__(self, name, level=10):
        self.name = name
        self.level = level

    def describe_wizard(self):
        """Show iformations about the wizard"""
        print("Here is the information about th wizard:")
        print(f"Name: {self.name}")
        print(f"Level: {self.level}\n")

    def level_up(self, new_level):
        """Increase the wizard's level"""
        self.level = new_level


# Creating a object to represent a wizard
merlin = Wizard("Merlin", 50)

# Describing the wizard before changing his level
merlin.describe_wizard()

# Changing the wizard's level through the method level_up
merlin.level_up(70)

# Describing the wizard after changing his level
merlin.describe_wizard()
