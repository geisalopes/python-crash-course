favorite_numbers = {
    "mandy": [42, 52],
    "micah": [23, 33, 43],
    "gus": [7, 8, 9, 10],
    "hank": [1_000_000, 2],
    "maggie": [0, -5, -10],
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"{number}")
