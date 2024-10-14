def city_country(city_name, city_country):
    """Return a string like 'Santiago, Chile'"""
    city_information = f"{city_name}, {city_country}"
    return city_information.title()


city = city_country("santiago", "chile")
print(city)
city = city_country("berlin", "germany")
print(city)
city = city_country("london", "england")
print(city)
