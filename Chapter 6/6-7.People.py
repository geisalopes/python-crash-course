# Make an empty list to store people in
people = []

# Define some people, and add them to the list
person = {
    "first_name": "geisa",
    "last_name": "lopes",
    "age": 40,
    "city": "sapucaia do sul",
}
people.append(person)

person = {
    "first_name": "diogo",
    "last_name": "sperb",
    "age": 45,
    "city": "novo hamburgo",
}
people.append(person)

person = {
    "first_name": "vilma",
    "last_name": "lopes",
    "age": 69,
    "city": "sao vicente",
}
people.append(person)

# Display all of the information in the dictionary
for person in people:
    name = person["first_name"].title() + " " + person["last_name"].title()
    age = str(person["age"])
    city = person["city"].title()

    print(name + ", of " + city + ", is " + age + " years old.")
