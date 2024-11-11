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


class IceCreamStand(Restaurant):
    """A simple class to describe a Ice Cream Stand"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes in the parent class."""
        """Then initialize attributes specific to an ice cream stand"""

        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["chocolate", "pitacchio", "black forest"]

    def describe_flavors(self):
        """Print a statement describing the available ice cream flavors"""
        print(f"\nThis is the ice cream flavors available:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")


my_restaurant = IceCreamStand("tribeca", "ice cream")
my_restaurant.describe_restaurant()
my_restaurant.describe_flavors()
