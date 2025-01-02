class Dragon:
    """A simple attempt to represent a dragon."""

    def __init__(self, name, color, age):
        """Initialize attributes to describe a dragon."""
        self.name = name
        self.color = color
        self.age = age

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.age}-year old {self.color} dragon named {self.name}"
        return long_name.title()

    def roar(self):
        """Print a statement showing the dragon's roar"""
        print(f"{self.name} lets out a thunderous roar!")

    def update_age(self, new_age):
        """Set the dragon's age to the given value"""
        if new_age >= self.age:
            self.age = new_age
            print(f"The dragon's age has been updated to {self.age} years!")
        else:
            print("You cant' make the dragon younger!")

    def grow_older(self, years):
        """Add the given amount of years to the dragon's age"""
        self.age += years
        print(f"Now the dragon's age has been updated to {self.age} years!")


class MagicGem:
    """A simple attempt to model a magic gem to a dragon"""

    def __init__(self, power_level=40):
        """Initialize the gem's attributes"""
        self.power_level = power_level

    def describe_gem(self):
        """Print a statement describing the gem's power level."""
        print(f"This dragon possesses a {self.power_level}-unit magic gem.")

    def get_magic_boost(self):
        """Print a statament about the magic boost this gem provides."""
        if self.power_level == 40:
            boost = 150
        elif self.power_level == 65:
            boost = 225

        print(f"This gem grants the dragon about {boost} extra power points.")


class Armor:
    """A simple attempt to model an armor for a dragon."""

    def __init__(self, protection_level=10):
        """Initialize the armor's attributes."""
        self.protection_level = protection_level

    def describe_armor(self):
        """Print a statement describing the armor."""
        print(
            f"The dragon is equipped with an armor of protection level {self.protection_level}."
        )

    def upgrade_armor(self):
        """Improve the armor's protection level."""
        self.protection_level += 5
        print(
            f"The armor has been upgraded! New protection level: {self.protection_level}"
        )


class FireDragon(Dragon):
    """Represent aspects of a dragon, specific to fire dragon."""

    def __init__(self, name, color, age):
        """Initialize attributes of the parent class"""
        super().__init__(name, color, age)
        self.magic_gem = MagicGem()
        self.armor = Armor()  # Composition: the dragon now has an Armor

    def breathe_fire(self):
        """Fire dragons can breathe fire."""
        print(f"{self.name} breathes a blazing inferno!")

    def get_descriptive_name(self):
        """Override to add 'Fire Dragon' in the description"""
        base_description = super().get_descriptive_name()
        return f"{base_description} (Fire Dragon)"


class IceDragon(Dragon):
    """Represent aspects of a dragon, specific to ice dragons."""

    def __init__(self, name, color, age):
        super().__init__(name, color, age)
        self.armor = Armor(protection_level=200)

    def roar(self):
        """Override to give a unique roar."""
        print(f"{self.name} lets out a cold and piercing roar!")


print("Creating a generic dragon:")
draco = Dragon("Draco", "green", 300)
print(draco.get_descriptive_name())  # Exibe: "300-Year-Old Green Dragon Named Draco"

print("\nCreating a fire dragon:")
smokey = FireDragon("Smokey", "red", 100)
print(
    smokey.get_descriptive_name()
)  # Exibe: "100-Year-Old Red Dragon Named Smokey (Fire Dragon)"
smokey.roar()
smokey.update_age(150)
smokey.grow_older(10)
smokey.magic_gem.describe_gem()
smokey.breathe_fire()
smokey.magic_gem.get_magic_boost()
print("\nCreating another fire dragon:")
blaze = FireDragon("Blaze", "golden", 200)
print(blaze.get_descriptive_name())
# Using the Armor
blaze.armor.describe_armor()
blaze.armor.upgrade_armor()
blaze.armor.describe_armor()

print("\nCreating a ice dragon:")
frost = IceDragon("Frost", "blue", 200)
print(frost.get_descriptive_name())
frost.roar()
