cities = {
    "berlin": {
        "country": "germany",
        "population": 1_000_000_000,
        "fact": "has more canals than Veneza",
    },
    "hamburg": {
        "country": "germany",
        "population": 3_000_000,
        "fact": "has a lot of crazy seagulls",
    },
    "london": {
        "country": "england",
        "population": 5_000_000,
        "fact": "has a lot of vegan places",
    },
}

for city, city_info in cities.items():
    print(f"\nCity: {city.title()}")
    country = city_info["country"]
    population = city_info["population"]
    fact = city_info["fact"]

    print(f"\tCountry: {country.title()}")
    print(f"\tPopulation: {population}")
    print(f"\tFact: {fact}")
