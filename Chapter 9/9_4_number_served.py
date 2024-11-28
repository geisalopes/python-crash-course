class Restaurant:
    """A simple description of a restaurant"""

    def __init__(self, name, cuisine):
        """Initialize name and type attributes"""
        self.name = name.title()
        self.cuisine = cuisine.title()
        self.number_served = 0

    def describe_restaurant(self):
        print(f"\nThe {self.name} is specialized in {self.cuisine} food.")

    def open_restaurant(self):
        print(f"\nThe {self.name} is open. Welcome!")

    def set_number_served(self, customers):
        self.number_served = customers

    def increment_number_served(self, increment):
        self.number_served += increment


restaurant = Restaurant("chay umi", "thai")
restaurant.describe_restaurant()

print(f"\nNumber served: {restaurant.number_served}")
restaurant.number_served = 500
print(f"Number served: {restaurant.number_served}")

restaurant.set_number_served(1000)
print(f"Number served: {restaurant.number_served}")

restaurant.increment_number_served(250)
print(f"Number served: {restaurant.number_served}")
