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
        print(f"The restaurant {self.restaurant} is open!")


new_restaurant = Restaurant("Chai Umy", "asian fusion")
new_restaurant.describe_restaurant()
new_restaurant.open_restaurant()
