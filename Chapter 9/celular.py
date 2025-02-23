class Battery:
    """Represents a cell phone's battery"""

    def __init__(self, capacity):
        self.capacity = capacity  # Capacity of the battery in mAh

    def describe_battery(self):
        """Display information about the battery"""
        print(f"This phone has a {self.capacity}mAh battery.")


class CellPhone:
    """Represents a cell phone"""

    def __init__(self, brand, model, battery_capacity):
        self.brand = brand
        self.model = model
        self.battery = Battery(
            battery_capacity
        )  # Creating a object Battery inside CellPhone class

    def describe_phone(self):
        """Display iformation about the cell phone"""
        print(f"Cellphone: {self.brand} {self.model}")
        self.battery.describe_battery()  # Accessing the battery method


# Creating a cellphone with a battery
my_phone = CellPhone("Samsung", "Galaxy S23", 5000)
my_phone.describe_phone()
