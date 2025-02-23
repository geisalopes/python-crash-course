class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def describe_product(self):
        print(f"{self.name} costs ${self.price}.")


class Manager:

    def __init__(self, name, store_name):
        self.name = name
        self.store_name = store_name

    def describe_manager(self):
        print(f"{self.name} is the manager the {self.store_name}.")
