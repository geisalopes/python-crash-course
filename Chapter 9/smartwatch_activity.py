class Smartwatch:

    def __init__(self, brand, model):
        """A simple class to describe the features of a smartwatch."""
        self.brand = brand.title()
        self.model = model
        self.steps_taken = 0

    def show_activity(self):
        """Display the watch's brand, model, and the total number of steps taken."""
        print(f"Watch's brand: {self.brand}")
        print(f"Watch's model: {self.model}")
        print(f"Number os steps: {self.steps_taken}\n")

    def increment_steps(self, increment_steps):
        """Increase the total number of steps. If the total exceeds 10,000, reset the steps."""
        new_steps = self.steps_taken + increment_steps
        if new_steps <= 10000:
            self.steps_taken = new_steps
            print(f"The total number of steps so far is: {self.steps_taken}")
        else:
            print("Step count limit reached. Resetting step counter...")

    def reset_steps(self):
        """Reset the step counter to zero."""
        self.steps_taken = 0
        print("\nResetting step counter...")
        print(f"Number of steps: {self.steps_taken}")


my_smartwatch = Smartwatch("apple", "skn080")
my_smartwatch.show_activity()
my_smartwatch.increment_steps(2000)
my_smartwatch.increment_steps(5000)
my_smartwatch.increment_steps(1234)
my_smartwatch.reset_steps()
