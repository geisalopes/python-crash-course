def make_album(artist, title):
    """Build a dictionary containing information about a music album"""
    album_dict = {"artist": artist.title(), "title": title.title()}
    return album_dict


album = make_album("ian gillan", "cherkazoo")
print(album)
album = make_album("ozzy osbourne", "no more tears")
print(album)
album = make_album("deep purple", "in rock")
print(album)
