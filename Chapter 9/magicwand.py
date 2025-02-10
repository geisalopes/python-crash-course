class MagicWand:

    def __init__(self, name, wood_type, core_material, power_level=10):
        self.name = name
        self.wood_type = wood_type
        self.core_material = core_material
        self.power_level = power_level

    def describe_wand(self):
        """Display information about the wand"""
        print(f"- Name: {self.name}")
        print(f"- Wood Type: {self.wood_type}")
        print(f"- Core Material: {self.core_material}")
        print(f"- Power Level: {self.power_level}\n")


snape_wand = MagicWand("Snape's Wand", "Oak", "Black Phoenix Feather", 0)
snape_wand.describe_wand()

snape_wand.power_level = 300
snape_wand.describe_wand()
