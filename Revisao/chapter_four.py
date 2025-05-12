# 🔁 1. for com range()

for numero in range(1, 6):
    print(numero)

print("-----------------------\n")

numeros = list(range(1, 12))
print(numeros)

print("-----------------------\n")


numeros = [1, 2, 3, 4, 5]
print(min(numeros))
print(max(numeros))
print(sum(numeros))

# 🍰 4. Fatiamento (slicing)
print("-----------------------\n")

nomes = ["ana", "bia", "carlos", "davi", "elisa"]
print(nomes[0:3])
print(nomes[:2])
print(nomes[-2:])

# ⚡ 5. List Comprehension
print("-----------------------\n")


quadrados = [x**2 for x in range(1, 6)]
print(quadrados)
