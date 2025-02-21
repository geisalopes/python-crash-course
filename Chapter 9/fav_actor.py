class Movie:
    """Represents a movie."""

    def __init__(self, title, year):
        self.title = title
        self.year = year

    def describe_movie(self):
        print(f"The movie '{self.title}' was released in {self.year}.")


class Actor:
    """Represents an actor with a list of movies."""

    def __init__(self, name):
        self.name = name
        self.movies = []  # Inicializa uma lista vazia de filmes

    def add_movie(self, movie):
        """Adds a movie (instance of Movie) to the actor's filmography."""
        self.movies.append(movie)

    def list_movies(self):
        """Prints all movies the actor has starred in."""
        print(f"\n{self.name} starred in the following movies:")
        for movie in self.movies:
            print(f"- {movie.title} ({movie.year})")


# Criando alguns filmes
movie1 = Movie("Love Actually", 2003)
movie2 = Movie("Die Hard", 1988)
movie3 = Movie("Harry Potter and the Philosopher's Stone", 2001)

# Criando o ator Alan Rickman
alan_rickman = Actor("Alan Rickman")

# Adicionando filmes à filmografia do ator
alan_rickman.add_movie(movie1)
alan_rickman.add_movie(movie2)
alan_rickman.add_movie(movie3)

# Exibindo os filmes do ator
alan_rickman.list_movies()
