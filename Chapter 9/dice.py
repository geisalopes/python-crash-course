import random


def roll_dice(sides):
    """Simula o lançamento de um dado de um número de lados especificado."""
    return random.randint(1, sides)


# Defina o número de jogadas e o número de lados do dado
num_rolls = 10
sides = 6

# Lista para armazenar os resultados
results = []

# Rolando os dados varias vezes
for roll in range(num_rolls):
    result = roll_dice(sides)
    results.append(result)
    print(f"Jogada {roll + 1}: {result}")

# Encontrando a jogada mais alta e mais baixa
highest_roll = max(results)
lowest_roll = min(results)

print("\n--- Resultados Finais ---")
print(f"Jogadas: {results}")
print(f"A jogada mais alta foi: {highest_roll}")
print(f"A jogada mais baixa foi: {lowest_roll}")
