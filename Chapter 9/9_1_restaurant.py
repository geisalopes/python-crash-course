class Restaurant:
    """A class representing restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant"""
        self.restaurant = restaurant_name.title()
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant"""
        print(
            f"The cuisine type of the restaurant {self.restaurant} is {self.cuisine}."
        )

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        print(f"The restaurant {self.restaurant} is open!")


new_restaurant = Restaurant("chai umy", "asian fusion")
new_restaurant.describe_restaurant()
new_restaurant.open_restaurant()
