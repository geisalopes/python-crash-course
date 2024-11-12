class Restaurant:
    """A simple description of a restaurant"""

    def __init__(self, name, cuisine):
        """Initialize name and type attributes"""
        self.name = name.title()
        self.cuisine = cuisine.title()

    def describe_restaurant(self):
        print(f"\nThe {self.name} is specialized in {self.cuisine} food.")

    def open_restaurant(self):
        print(f"\nThe {self.name} is open. Welcome!")


restaurant = Restaurant("chay umi", "thai")
print(restaurant.name)
print(restaurant.cuisine)
restaurant.describe_restaurant()
restaurant.open_restaurant()
