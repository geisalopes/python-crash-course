class Restaurant:
    """Creating a simple restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Describing the restaurant"""
        self.restaurant = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        print(
            f"The cuisine type of the restaurant {self.restaurant} is {self.cuisine}."
        )

    def open_restaurant(self):
        print(f"The restaurant {self.restaurant} is open!\n")


asian_restaurant = Restaurant("Chai Umy", "asian fusion")
italian_restaurant = Restaurant("Da Ponte", "italian")
fast_food_restaurant = Restaurant("Swing Kitchen", "fast food")

asian_restaurant.describe_restaurant()
asian_restaurant.open_restaurant()

italian_restaurant.describe_restaurant()
italian_restaurant.open_restaurant()

fast_food_restaurant.describe_restaurant()
fast_food_restaurant.open_restaurant()
