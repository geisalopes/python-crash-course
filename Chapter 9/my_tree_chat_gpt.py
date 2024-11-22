class Tree:

    def __init__(self, name, location):
        self.name = name.title()
        self.location = location.title()
        self.height = 0

    def describe_tree(self):
        """A simple methos to describe a tree and its location"""
        print(
            f"My favorite tree is a {self.name} and it is located in {self.location}."
        )

    def set_height(self, height):
        """Set the height of the tree, ensuring it is at least 1 meter."""
        if height >= 1:
            self.height = height
            print(f"My dear {self.name} hat {self.height} meters height.")
        else:
            print("Error: a tree can't have less them 1 meter.")

    def grow_tree(self, grow):
        """Increase the height of the tree, up to a maximum of 100 meters."""
        new_size = self.height + grow
        if new_size > 100:
            print(
                "The maximum height has been reached. The tree cant' grow more than 100 meters."
            )
            self.height = 100
        else:
            self.height = new_size
            print(f"My dear {self.name} has reached a size of {self.height} metres.")


my_favorite_tree = Tree("beech", "tiergarten")
my_favorite_tree.describe_tree()
my_favorite_tree.set_height(3)
my_favorite_tree.grow_tree(80)
my_favorite_tree.grow_tree(200)
