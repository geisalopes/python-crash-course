teachers = {
    "minerva": {
        "house": "gryffindor",
        "teaches": "tranfiguration",
        "patronus": "cat",
    },
    "severus": {
        "house": "slytherin",
        "teaches": "potions",
        "patronus": "deer",
    },
    "pomona": {
        "house": "hufflepuffle",
        "teaches": "herbology",
        "patronus": "hedgehog",
    },
}

for teacher, teacher_info in teachers.items():
    print(f"\nThis is the information about professor {teacher.title()}:")
    house = teacher_info["house"]
    teaches = teacher_info["teaches"]
    patronus = teacher_info["patronus"]

    print(f"\tHouse: {house.title()}")
    print(f"\tTeaches: {teaches.title()}")
    print(f"\tPatronus: {patronus.title()}")
