def make_album(artist_name, album_title):
    """Return a dictionary of information about a music album"""
    artist_album = {"artist": artist_name.title(), "album": album_title.title()}
    return artist_album


while True:
    print("\nPlease tell me more about your favorite artist: ")
    print("(enter 'q' at any time to quit)")

    artist = input("\nArtist's name: ")
    if artist == "q":
        break
    album = input("Album's name: ")
    if album == "q":
        break

    album_info = make_album(artist, album)
    print(f"Here is the information about your artist: {album_info}")

print("Thanks for responding.")
