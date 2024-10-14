def make_album(artist_name, album_title, number_of_songs=None):
    """Return a dictionary with information about a music album"""
    artist_album = {"artist": artist_name.title(), "album": album_title.title()}
    if number_of_songs:
        artist_album["songs"] = number_of_songs
    return artist_album


album_info = make_album("ian gillan", "cherkazoo", number_of_songs=10)
print(album_info)
album_info = make_album("ozzy osbourne", "no more tears")
print(album_info)
album_info = make_album("deep purple", "in rock", number_of_songs=7)
print(album_info)
