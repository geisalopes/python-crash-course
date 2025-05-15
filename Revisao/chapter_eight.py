# 🔧 1. Criando uma função


def greeting():
    print("Hello, welcome!")


greeting()

print("--------------------\n")

# 🧑‍🎓 2. Passando informações (argumentos)


def greeting_name(name):
    print(f"Hello, {name.title()}!")


greeting_name("geisa")

print("--------------------\n")
# 📦 3. Argumentos posicionais vs nomeados


def describe_animal(type, name):
    print(f"\nI have an/a {type}.")
    print(f"Its name is {name.title()}.")


# Posicional
describe_animal("cat", "nianko-sensei")

# Nomeado
describe_animal(type="cat", name="nianko-sensei")


print("--------------------\n")
# 💬 4. Valor padrão


def describe_animal(name, type="cat"):
    print(f"\nI have an/a {type}.")
    print(f"Its name is {name.title()}.")


# Sem declarar o tipo
describe_animal("nianko-sensei")

# Declarando o tipo
describe_animal("nianko-sensei", "dog")

print("--------------------\n")
# 🔄 5. Retornando valores


def full_name(name, surname):
    return f"{name} {surname}".title()


full_name("geisa", "lopes")


print("--------------------\n")
# 📚 6. Passando listas para funções


def greeting_names(names):
    for name in names:
        print(f"Hello, {name.title()}!")


friends = ["magda", "tina"]
greeting_names(friends)

print("--------------------\n")
# ✅ 7. Funções com número arbitrário de argumentos


def make_pizza(*ingredients):
    print("Making pizza with:")
    for ingridient in ingredients:
        print(f"- {ingridient.title()}")


make_pizza("broccoli", "thun-vish", "caperns")
