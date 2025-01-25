class Plant:
    """A simple class representing a plant"""

    def __init__(self, name, plant_type, size, watered_status="watered"):
        self.name = name
        self.plant_type = plant_type
        self.size = size
        self.watered_status = watered_status

    def describe_plant(self):
        """Describe the plant"""
        print("\nInformation about your plant...")
        print(
            f"The {self.name} is a plant of the {self.plant_type} type, it is {self.size} tall and is currently {self.watered_status}."
        )

    def water_plant(self, new_status):
        """Update the watered status of the plant"""
        self.watered_status = new_status
        print(f"{self.name} is now {self.watered_status}.")


# Creating instances with the basic value of watered status.
ficus = Plant("Ficus", "ficuslyarata", "130 cm")
zz = Plant("ZZ", "zamioculcas", "40 cm")

# Creating an instance with a personalized value for the watered status.
snake_plant = Plant("Snake Plant", "sanseviera", "50 cm", watered_status="not watered")

# Calling the method describe_plant for each object.
ficus.describe_plant()
zz.describe_plant()
snake_plant.describe_plant()

# Updating the watered_status of the Snake Plant.
snake_plant.water_plant("watered")
