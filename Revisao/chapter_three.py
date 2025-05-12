# Listas

frutas = ["apple", "banana", "orange"]
print(frutas[0])
print(frutas[1])
print(frutas[-1])

print("-----------------------\n")

frutas[1] = "mango"

print(frutas[0])
print(frutas[1])
print(frutas[-1])

print("-----------------------\n")

print(frutas)

frutas.append("kiwi")  # adiciona no fim
frutas.insert(0, "abacaxi")  # insere no indice 0

print(frutas)

print("-----------------------\n")

print(frutas)
del frutas[2]  # remove por indice
print(frutas)

frutas.remove("apple")  # remove por valor
print(frutas)

frutas.pop()  # remove o último e retorna
print(frutas)

frutas.pop(0)  # remove o índice 0 e retorna
print(frutas)

print("-----------------------\n")

frutas.append("kiwi")
frutas.append("mango")
frutas.append("banana")

for fruta in frutas:
    print(f"Gosto de {fruta.title()}")
