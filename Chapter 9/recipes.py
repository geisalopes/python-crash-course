class Recipe:
    """A simple attempt to represent a recipe book"""

    def __init__(self, name, cuisine, difficulty, tested=False):
        self.name = name.title()
        self.cuisine = cuisine.title()
        self.difficulty = difficulty.title()
        self.tested = tested

    def describe_recipe(self):
        """Show details about the recipe"""
        print("Information about the recipe:")
        print(f"- Name: {self.name}")
        print(f"- Cuisine: {self.cuisine}")
        print(f"- Difficulty: {self.difficulty}")
        print(f"- Tested: {'Yes' if self.tested else 'No'}\n")

    def mark_as_tested(self):
        "Mark the recipe as tested"
        self.tested = True
        print(f"The recipe {self.name} has been marked as tested.\n")


# Creating instances of the class Recipe
recipe1 = Recipe("pasta al pesto", "italian", "medium")
recipe2 = Recipe("thuna sandwich", "mediterranean", "easy")
recipe3 = Recipe("lamen", "chinese", "medium", tested=True)

# Calling the method describe_recipe for each instance
recipe1.describe_recipe()
recipe2.describe_recipe()
recipe3.describe_recipe()

# Calling the method mark_as_tested for recipe 1
recipe1.mark_as_tested()

# Display updated information for recipe1
recipe1.describe_recipe()
