def city_names(city, country):
    place = f"{city} {country}"
    return place

place_1 = city_names("ocotlan", "jalisco")
print(place_1)

place_2 = city_names("Jamay", "Jalisco")
print(place_2)

place_3 = city_names("Cuitzeo", "Jalisco")
print(place_3)

def music_albums(album, artist, tracks = ""):
    if tracks:
        data = {"Album: ": album, "Artist: ": artist, "Tracks: ": tracks}
    else:
        data = {"Album: ": album, "Artist: ": artist}
    return data


record_1 = music_albums("The great cold distance.", "Katatonia", "10")
record_2 = music_albums("God hates us all", "Slayer")
record_3 = music_albums("Eaten back to life", "Cannibal Corpse")

print(record_1, record_2, record_3)

while True:
    print("Input your favourite album info.")
    print("Input 'Q' at any time to exit")
    album = input("\nAlbum?: ").title()
    if album == "Q":
        break
    artist = input("\nArtist?: ").title()
    if artist =="Q":
        break
    tracks = input("\nTracks?: ").title()
    if tracks == "Q":
        break

    info = music_albums(album, artist, tracks = "")

    print(f"{info}")