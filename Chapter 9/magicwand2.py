class MagicWand:

    def __init__(self, name, wood_type, core_material, power_level=10):
        self.name = name
        self.wood_type = wood_type
        self.core_material = core_material
        self.power_level = power_level

    def describe_wand(self):
        """Display information about the wand"""
        print(f"- Name: {self.name}")
        print(f"- Wood Type: {self.wood_type}")
        print(f"- Core Material: {self.core_material}  ")
        print(f"- Power Level: {self.power_level}\n")

    def increase_power(self, amount):
        """Increase the wand's power level"""
        if self.power_level + amount > 100:
            self.power_level = 100
            print(f"The power of {self.name} is at its maximum! (100)")
        else:
            self.power_level += amount
            print(f"The power of {self.name} has increased to {self.power_level}.")


# Creating a wand
elder_wand = MagicWand("Elder Wand", "Elder Wood", "Thestral Tail Hair", 80)

# Describing the wand before modifying it
elder_wand.describe_wand()

# Using the method to increase the wand's power
elder_wand.increase_power(15)  # The currently value is 80, so it goes to 95
# Calling the method describe_wand after change its power level
elder_wand.describe_wand()

# Using the method to increase the wand's power again
elder_wand.increase_power(10)  # It goes now to 105, but the maximum is 100book
# Calling again the method describe_wand after change its power level
elder_wand.describe_wand()
