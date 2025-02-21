class Movie:
    def __init__(self, title, year):
        self.title = title
        self.year = year


class Actress:
    def __init__(self, name, movie):
        self.name = name
        self.movie = movie

    def describe_actress(self):
        print(f"{self.name} starred in '{self.movie.title}' ({self.movie.year}).")


movie1 = Movie("Mamma Mia!", 2008)
movie2 = Movie("Alien", 1979)

actress1 = Actress("Meryl Streep", movie1)
actress2 = Actress("Sigourney Weaver", movie2)

actress1.describe_actress()
actress2.describe_actress()
