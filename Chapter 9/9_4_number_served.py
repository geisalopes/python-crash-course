class Restaurant:
    """A class representing restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant"""
        self.restaurant = restaurant_name.title()
        self.cuisine = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summary of the restaurant"""
        print(
            f"The cuisine type of the restaurant {self.restaurant} is {self.cuisine}."
        )

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        print(f"The restaurant {self.restaurant} is open!")

    def set_number_served(self, number_served):
        """Allow user to set the number os customer that have been served"""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """Allow user to increment the number of customers served."""
        self.number_served += additional_served


restaurant = Restaurant("chai umy vegan", "asian fusion")
restaurant.describe_restaurant()

print(f"\nNumber served: {restaurant.number_served}")
restaurant.number_served = 500
print(f"Number served: {restaurant.number_served}")

restaurant.set_number_served(1000)
print(f"Number served: {restaurant.number_served}")

restaurant.increment_number_served(250)
print(f"Number served: {restaurant.number_served}")
