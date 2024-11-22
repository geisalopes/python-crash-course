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

    def set_number_served(self, guests):
        """Define the number of guests served"""
        self.number_served = guests
        print(f"The number of served guests is {self.number_served}.")

    def increment_number_served(self, number):
        self.number_served += number
        print(f"Update number of served guests: {self.number_served}")


restaurant = Restaurant("chay umi", "thai")
restaurant.describe_restaurant()
restaurant.number_served = 50

restaurant.set_number_served(100)

restaurant.increment_number_served(50)
