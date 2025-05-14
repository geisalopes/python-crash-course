# 🧪 1. Testes condicionais

carro = "audi"
print(carro == "audi")  # True
print(carro == "bmw")  # False

# 📦 3. Testando se valor está em uma lista

frutas = ["banana", "apple"]
print("apple" in frutas)  # True
print("orange" not in frutas)  # True

# 🧭 4. Estruturas if, elif, else

idade = 19

if idade < 18:
    print("Menor de idade")
elif idade == 18:
    print("Tem 18 anos.")
else:
    print("Maior de idade")
