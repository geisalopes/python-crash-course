class Battery:

    def __init__(self, capacity):
        self.capacity = capacity  # Stores battery capacity

    def describe_battery(self):
        print(f"This battery has {self.capacity}mAh.")


# Creating a battery
# battery = Battery(5000) # Ao inves de criar o objeto aqui fora da classe, eu coloquei ele dentro da classe Cellphone
# battery.describe_battery() # Ao inves de chamar o metodo daqui, eu chamo ele de dentro da class Cellphone. com a diferenca de colocar um self. antes do restante (self.battery.describe_battery())


class CellPhone:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.battery = Battery(5000)  # Creating a Battery object within Cellphone

    def describe_phone(self):
        print(f"Cellphone: {self.brand} {self.model}")
        self.battery.describe_battery()  # Calling the battery method inside the mobile phone


# Creating the cellphone (now with battery)
my_phone = CellPhone("Samsumg", "Galaxy S23")
my_phone.describe_phone()
my_replacement_battery = Battery(10000)
my_phone.battery = my_replacement_battery
