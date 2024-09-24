favorite_pizzas = ["diavola", "marguerita", "toscana"]
friends_pizzas = favorite_pizzas[:]

favorite_pizzas.append("veggie lover's")
friends_pizzas.append("marinara")

print("My favorite pizzas are:")
for pizza in favorite_pizzas:
    print("- " + pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friends_pizzas:
    print("- " + pizza)
