class Playlist:

    def __init__(self, name):
        """Initialize the playlist with a name and an empty list of songs."""
        self.name = name.title()
        self.songs = []

    def add_song(self, song):
        """Add a song to the playlist."""
        self.songs.append(song.title())
        print(f"Adding '{song.title()}' to the playlist.")

    def remove_song(self, song):
        """Remove a song from the playlist if it exists."""
        if song.title() in self.songs:
            self.songs.remove(song.title())
            print(f"Removing '{song.title()}' from the playlist. ")
        else:
            print(f"'{song.title()}' is not in the playlist.")

    def show_songs(self):
        """Show all songs in the playlist."""
        if not self.songs:
            print("The playlist is empty.")
        else:
            print(f"\nSongs in the playlist '{self.name}':")
            for index, song in enumerate(self.songs, 1):
                print(f"{index}. {song}")

    def total_songs(self):
        """Return the total number of songs in the playlist."""
        return len(self.songs)

    def clear_playlist(self):
        """Remove all songs from the playlist."""
        self.songs.clear()
        print("The playlist has been cleared.")


my_playlist = Playlist("My Favorites")

my_playlist.add_song("Aces High")
my_playlist.add_song("she took my breath alway")
my_playlist.add_song("suburbia")
my_playlist.add_song("ariel")

my_playlist.show_songs()

my_playlist.remove_song("ariel")
my_playlist.remove_song("black night")

print(f"\nTotal songs in '{my_playlist.name}': {my_playlist.total_songs()}")

my_playlist.clear_playlist()

my_playlist.show_songs()
