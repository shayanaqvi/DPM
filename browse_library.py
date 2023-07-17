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
                artists_table = generate_table("Artists", artists, "artist")
                console.print(artists_table)
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
                        temporary_current_album = album["album"]
                        albums_by_artist.append(album)
                albums_by_artist_table = generate_table(user_selection_lvl_2, albums_by_artist, "album")
                console.print(albums_by_artist_table)
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
                titles_from_album_table = generate_table(f"{user_selection_lvl_4} - {user_selection_lvl_2}", titles_from_album, "title")
                console.print(titles_from_album_table)
                current_level = 6
            case 6:
                # Level 6: get input from user
                try:
                    user_input_lvl_6 = input("Do: ")
                    handle_user_input(user_input_lvl_6, titles_from_album, "title", user_selection_lvl_4)
                except (KeyboardInterrupt, EOFError):
                    cs()
                    current_level = 3


def generate_table(title, list_of_media, type_of_media):
    table = Table(
        box=box.SIMPLE,
        style="cyan"
    )
    table.add_column(
        "#",
        header_style=colours["accent1"],
        style=colours["accent1"]
    )
    table.add_column(
        title,
        header_style=colours["accent1"],
    )
    display_index = 1

    for item in list_of_media:
        table.add_row(
            str(display_index),
            item[type_of_media]
        )
        display_index += 1

    return table


def handle_user_input(user_input, list_of_media, type_of_media, album_name=""):
    global current_level
    user_input_array = []
    for item in user_input.split(" "):
        user_input_array.append(item)

    match len(user_input_array):
        case 1:
            try:
                if user_input_array[0].isdigit():
                    if current_level == 6:
                        info_panel("This operation is not supported here", "error")
                    else:
                        selection = list_of_media[int(user_input_array[0]) - 1]
                        current_level += 1
                        return selection
                elif user_input_array[0] == "a":
                    info_panel("Index not provided", "error")
                else:
                    info_panel("Invalid selection", "error")
            except (IndexError):
                info_panel("This index does not exist", "error")
        case 2:
            match user_input_array[0]:
                case "a":
                    if user_input_array[1].isdigit():
                        if current_level == 6:
                            selection = list_of_media[int(user_input_array[1]) - 1]
                            client.findadd("album", album_name, type_of_media, selection[type_of_media])
                            info_panel("Selection added to queue", "affirmative")
                        else:
                            selection = list_of_media[int(user_input_array[1]) - 1]
                            client.findadd(type_of_media, selection[type_of_media])
                            info_panel("Selection added to queue", "affirmative")
                    elif user_input_array[1] == "":
                        info_panel("Index not provided", "error")
                    else:
                        info_panel("Invalid selection", "error")
                case _:
                    info_panel("Invalid operation", "error")
        case _:
            info_panel("Invalid operation", "error")


