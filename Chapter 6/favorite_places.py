favorite_places = {
    "cristina": ["italy", "romania", "belgium"],
    "magdalena": ["polen", "germany", "cuba"],
    "helga": ["hungaria", "france", "london"],
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")
