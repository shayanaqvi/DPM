from cs import cs
from client import client
from info_panel import info_panel
from Menu import Menu
from Colours import colours

from rich import box
from rich.console import Console
from rich.table import Table
from rich.panel import Panel


menu = Menu()
console = Console()
current_level = 1


def browse_library():
    global current_level
    while True:
        match current_level:
            case 1:
                # Level 1: display all artists in the library
                cs()
                artists = client.list("artist")
                for artist in artists:
                    console.print(artist["artist"])
                current_level = 2
            case 2:
                # Level 2: get input from user
                try:
                    user_input_lvl_2 = input("Do: ")
                    user_selection_lvl_2_raw = handle_user_input(user_input_lvl_2, artists, "artist")
                except (KeyboardInterrupt, EOFError):
                    cs()
                    return
            case 3:
                # Level 3: display albums from the selected artist
                cs()
                user_selection_lvl_2 = user_selection_lvl_2_raw["artist"]
                albums_by_artist_raw = client.find("artist", user_selection_lvl_2)
                albums_by_artist = []
                # this variable will ensure that the same album isn't printed multiple times
                temporary_current_album = ""
                for album in albums_by_artist_raw:
                    if album["album"] == temporary_current_album:
                        pass
                    else:
                        console.print(album["album"])
                        temporary_current_album = album["album"]
                        albums_by_artist.append(album)
                current_level = 4
            case 4:
                # Level 4: get input from user
                try:
                    user_input_lvl_4 = input("Do: ")
                    user_selection_lvl_4_raw = handle_user_input(user_input_lvl_4, albums_by_artist, "album")
                except (KeyboardInterrupt, EOFError):
                    cs()
                    current_level = 1
            case 5:
                # Level 5: display tracks from the selected album
                cs()
                user_selection_lvl_4 = user_selection_lvl_4_raw["album"]
                titles_from_album = client.find("album", user_selection_lvl_4)
                for title in titles_from_album:
                    console.print(title["title"])
                current_level = 6
            case 6:
                # Level 6: get input from user
                try:
                    user_input_lvl_6 = input("Do: ")
                    handle_user_input(user_input_lvl_6, titles_from_album, "title")
                except (KeyboardInterrupt, EOFError):
                    cs()
                    current_level = 3


def handle_user_input(user_input, list_of_media, type_of_media):
    global current_level
    user_input_array = []
    for item in user_input.split(" "):
        user_input_array.append(item)

    match len(user_input_array):
        case 1:
            try:
                if user_input_array[0].isdigit():
                    selection = list_of_media[int(user_input_array[0]) - 1]
                    current_level += 1
                    return selection
            except (IndexError):
                info_panel("This index does not exist")
        case 2:
            match user_input_array[0]:
                case "a":
                    if user_input_array[1].isdigit():
                        selection = list_of_media[int(user_input_array[1]) - 1]
                        client.findadd(type_of_media, selection[type_of_media])
                        info_panel("Selection added to queue")
                    else:
                        info_panel("Invalid selection")
                case _:
                    info_panel("Invalid operation")
        case _:
            info_panel("Invalid operation")


browse_library()
