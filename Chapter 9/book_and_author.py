class Movie:
"""Represents a movie."""

    def __init__(self, title, year):
        self.title = title
        self.year = year

    def describe_movir (self):
        print(f"My favorite actor are {self.title}, released in {self.year}.")

class Actor:
    def __init__(self, name, movies):
        self.name = name
        self.movies = movies

    def list_movies(self):
        print(f"{self.name} made the following movies: {self.movies}")


my_movie = Movie("Love Actually, 2005")
my_actor = Actor("Alan, Rickman,")
