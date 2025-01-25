class VideoGame:
    """A simple class to represent a videogame"""

    def __init__(self, title, genre, platform, rating="not rated"):
        self.title = title.title()
        self.genre = genre.title()
        self.platform = platform.title()
        self.rating = rating

    def describe_game(self):
        """Show details about the game"""
        print("Here is the information about your game:")
        print(f"- Title: {self.title}")
        print(f"- Genre: {self.genre}")
        print(f"- Platform: {self.platform}")
        print(f"- Rating: {self.rating}\n")

    def update_rating(self, new_rating):
        """Update the game's rating status"""
        self.rating = new_rating
        print(f"The rating of the game {self.title} was updated to: {self.rating}")


# Creating objects(instances) with the dafault rating

game1 = VideoGame("okami", "rpg", "nintendo switch")
game2 = VideoGame("kirby forgotten land", "adventure", "nintedo switch")

# Creating a instance with a personalized value for rating
game3 = VideoGame("mario kart", "racing", "nintendo switch", rating="very good")

# Calling the method describe_game for each instance
game1.describe_game()
game2.describe_game()
game3.describe_game()

# Calling the method update_rating for the game Okami
game1.update_rating(new_rating="superb")
