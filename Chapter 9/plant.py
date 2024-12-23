class Plant:
    """A simple attempt to represent a plant."""

    def __init__(self, name, species, water_needed):
        """Initialize attributes to describe a plant."""
        self.name = name
        self.species = species
        self.water_needed = water_needed

    def get_plant_info(self):
        """Return a neatly formatted description of the plant."""
        info = f"{self.name} is a {self.species} plant that needs {self.water_needed} liters of water."
        return info.title()

    def water_plant(self, water_given):
        """Print a statement showing if the plant has been watered enough."""
        if water_given >= self.water_needed:
            print(f"{self.name} has been watered enough!")
        else:
            print(f"{self.name} needs more water!")


class CarnivorousPlant(Plant):
    """Represent aspects of a plant, specific to carnivorous plants."""

    def __init__(self, name, species, water_needed, food_type):
        """
        Initialize attributes of the parent class and new attributes for carnivorous plants.
        """
        super().__init__(name, species, water_needed)
        self.food_type = food_type  # The type of food the carnivorous plant consumes (e.g., insects, flies)

    def describe_feeding(self):
        """Print a statement describing how the plant gets its nutrients."""
        print(f"This plant eats {self.food_type} to get its nutrients.")


# Criando uma planta carnívora
venus_flytrap = CarnivorousPlant("Venus Flytrap", "Dionaea Muscipula", 0.5, "insects")

# Exibindo as informações sobre a planta
print(venus_flytrap.get_plant_info())

# Descrevendo como a planta se alimenta
venus_flytrap.describe_feeding()

# Testando o método de rega
venus_flytrap.water_plant(0.6)
