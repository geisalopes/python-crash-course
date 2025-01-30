class Potion:
    """A simple class representing potions."""

    def __init__(self, name, effect, rarity="common", used=False):
        self.name = name.title()
        self.effect = effect.title()
        self.rarity = rarity.title()
        self.used = used

    def describe_potion(self):
        """Display information about rhe potion"""
        print(f"Name: {self.name}")
        print(f"Information about '{self.name}':")
        print(f"- Effect: {self.effect}")
        print(f"- Rarity: {self.rarity}")
        print(f"- Used: {'Yes' if self.used else 'No'}\n")

    def use_potion(self):
        """Mark the potion as used"""
        self.used = True
        print(f"The potion {self.name} has been marked as used.\n")

    def upgrade_rarity(self, new_rarity_status):
        """Change the rarity status of the potion"""
        self.rarity = new_rarity_status
        print(f"The rarity status of {self.name} has been updated to {self.rarity}.")


# Creating instances of the class Potion
potion1 = Potion(
    "Polyjuice Potion",
    "Allows the person who drinks it to take the form of another person.",
    rarity="Very Rare",
)
potion2 = Potion("Amortentia", "An extremely powerful love potion.")
potion3 = Potion(
    "Felix Felicis",
    "Grants extreme luck for a period of time.",
    used=True,
)
# Calling the method describe_recipe for each instance
potion1.describe_potion()
potion2.describe_potion()
potion3.describe_potion()

# Calling the method upgrade_rarity for potion3
potion3.upgrade_rarity("Extremely Rare")

# Display updated information for potion3
potion3.describe_potion()
