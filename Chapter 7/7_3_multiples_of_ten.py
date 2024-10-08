number = input("Tell me a number and I tell you if it is multiple of ten or not: ")
number = int(number)

if number % 10 == 0:
    print(f"\nThe number {number} is multiple of ten.")
else:
    print(f"The number {number} is not a multiple of ten.")
