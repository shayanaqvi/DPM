from client import client

def queue():
    current_song = client.currentsong()
    current_playlist = client.playlistinfo()

    current_playlist_array = []
    display_playlist_array = []

    cs_index = 0

    for item in current_playlist:
        current_playlist_array.append(item)

    for item in current_playlist_array:
        if item["title"] == current_song["title"]:
            cs_index = current_playlist_array.index(item)
        display_playlist_array.append(item["title"])

    # print everything ahead of current index
    for item in display_playlist_array[cs_index:]:
        print(item)

    temp = input("")
