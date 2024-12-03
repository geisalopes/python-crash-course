class Plant:

    def __init__(self, name, species):
        "A simple class to track a plant and its water needs"
        self.name = name.title()
        self.species = species.title()
        self.water_level = 0

    def display_status(self):
        """Displays the name of the plant, its species, and the water level"""
        print("Here is the information about my plant:")
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        print(f"Water Level: {self.water_level}\n")

    def water_plant(self, amount):
        """Increment the total amount of watering. If it exceeds 10, warn the user."""
        if self.water_level + amount > 10:
            print("The water level can't exceed 10. Stop watering your plant.")
        else:
            self.water_level += amount
            print(f"My plant was watered. New level of water: {self.water_level}")

    def reset_water_level(self):
        """Reset the level of watering to zero"""
        self.water_level = 0
        print(
            f"\n It's a new week! The plant's water level has been reset to {self.water_level}."
        )


my_plant = Plant("moonstone", "cactus")
my_plant.display_status()

my_plant.water_plant(5)
my_plant.water_plant(3)
my_plant.water_plant(2)
my_plant.water_plant(7)

my_plant.reset_water_level()
