prompt = "\nPlease enter your favorite toppings: "
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    toppings = input(prompt)
    if toppings != "quit":
        print(f"\n I will add {toppings} to your pizza.")
    else:
        break
