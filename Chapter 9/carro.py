class Car:

    def __init__(self, model, color):
        """A simple class to describe a car"""
        self.model = model
        self.color = color
        self.mileage = 0

    def describe_car(self):
        """Shows the information about the car"""
        print(f"Car: {self.model}, Color: {self.color}, Mileage: {self.mileage}")

    def update_mileage(self, actual_mileage):
        if actual_mileage <= self.mileage:
            print("Error: the actual mileage can't be less than the previous mileage!")
        else:
            self.mileage = actual_mileage
            print(f"The actual mileage of my {self.model} is {self.mileage}.")

    def increment_mileage(self, increment):
        self.mileage += increment
        if self.mileage > 300_000:
            print("Error: the car has reached the maximum mileage. Try again.")
        else:
            print(f"The actual mileage of my {self.model} is now {self.mileage}")


my_car = Car("Aston Martin", "teal")
my_car.describe_car()
my_car.update_mileage(300)
my_car.increment_mileage(300_000)
