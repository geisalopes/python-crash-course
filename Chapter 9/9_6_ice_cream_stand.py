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


class IceCreamStand(Restaurant):
    """Represent an ice cream stand."""

    def __init__(self, name, cuisine="ice_cream"):
        super().__init__(name, cuisine)
        self.flavors = []

    def display_flavors(self):
        print(f"Ice cream flavors available:")
        for flavor in self.flavors:
            print("- " + flavor.title())


vegancream = IceCreamStand("Tribecca")
vegancream.flavors = ["chocolate", "vanilla", "strawberry", "pistacchio"]
vegancream.describe_restaurant()
vegancream.display_flavors()
