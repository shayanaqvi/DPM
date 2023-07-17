import sys

from info_panel import info_panel
from client import client
from Colours import colours

from rich import box
from rich.console import Console
from rich.table import Table

console = Console()


def playlist_menu():
    # view, load and save playlists (no management (yet))
    # use command line arguments
    user_arg = sys.argv
    match len(user_arg):
        case 1:
            info_panel("Please provide an argument\nInput 'dpm help' for more information", "information")
        case 2:
            handle_arguments(user_arg)
        case _:
            info_panel("Invalid operation", "error")


def handle_arguments(argument):
    opt = argument[1]
    match opt:
        case "l":
            current_level = 1
            # view/load playlists
            while True:
                match current_level:
                    case 1:
                        stored_playlists_raw = client.listplaylists()
                        stored_playlists = []
                        for item in stored_playlists_raw:
                            stored_playlists.append(item["playlist"])
                        table = generate_table(stored_playlists)
                        console.print(table)
                        current_level = 2
                    case 2:
                        user_input = input("Choose: ")
                        handle_input(user_input, stored_playlists)
        case "s":
            # save playlist
            pass


def handle_input(user_input, list_of_playlists):
    user_input_array = []
    for item in user_input.split(" "):
        user_input_array.append(item)

    match len(user_input_array):
        case 1:
            info_panel("This operation is not supported here", "error")
        case 2:
            match user_input_array[0]:
                case "a":
                    if user_input_array[1].isdigit():
                        client.load(list_of_playlists[int(user_input_array[1]) - 1])
                        info_panel("Playlist loaded", "affirmative")
                    elif user_input_array[1] == "":
                        info_panel("Index not provided")
                case _:
                    pass
        case _:
            pass


def generate_table(list_of_playlists):
    table = Table(
        box=box.SIMPLE,
        style=colours["accent1"]
    )
    table.add_column(
        "#",
        header_style=colours["accent1"],
        style=colours["accent1"]
    )
    table.add_column(
        "Playlist",
        header_style=colours["accent1"],
    )
    display_index = 1

    for playlist in list_of_playlists:
        table.add_row(
            str(display_index),
            playlist
        )
        display_index += 1

    return table


playlist_menu()
