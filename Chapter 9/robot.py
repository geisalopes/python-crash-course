class Robot:
    """A simple attempt to represent a robot"""

    def __init__(self, name, function, battery_level=100):
        self.name = name.title()
        self.function = function.title()
        self.battery_level = battery_level

    def describe_robot(self):
        """Show details about the robot"""
        print("Here is the information about your robot:")
        print(f"Name: {self.name}")
        print(f"Function: {self.function}")
        print(f"Battery Level: {self.battery_level}%\n")

    def use_battery(self, new_battery_level):
        self.battery_level = new_battery_level
        if self.battery_level < 30:
            print(
                f"The battery level of {self.name} is in {self.battery_level}%. You need to recharge it."
            )
        else:
            print(f"The battery level of {self.name} is still good.")


# Creating instances(objects) from the class Robot
r2 = Robot("r2", "cook")
c3po = Robot("c3po", "translator")

# Creating a instance with a personalized value for battery_level
r3 = Robot("r3", "driver", battery_level=50)

# Calling the method describe_robot
r2.describe_robot()
c3po.describe_robot()
r3.describe_robot()

#  Calling the method use_battery for r3
r3.use_battery(new_battery_level=20)

#  Calling the method use_battery for c3po
c3po.use_battery(new_battery_level=75)
