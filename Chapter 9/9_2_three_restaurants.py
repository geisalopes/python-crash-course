class Restaurant:
    """A simple description of a restaurant"""

    def __init__(self, name, cuisine):
        """Initialize name and type attributes"""
        self.name = name.title()
        self.cuisine = cuisine.title()

    def describe_restaurant(self):
        print(f"\nThe {self.name} is specialized in {self.cuisine}.")

    def open_restaurant(self):
        print(f"\nThe {self.name} is open. Welcome!")


thai_restaurant = Restaurant("chay umi", "thai food")
thai_restaurant.describe_restaurant()

italian_restaurant = Restaurant("the sanctuary", "croissants")
italian_restaurant.describe_restaurant()

donuts_restaurant = Restaurant("brammibal's", "vegan donuts")
donuts_restaurant.describe_restaurant()
