from info_panel import info_panel
from client import client
from cs import cs
from Colours import colours

from rich import box
from rich.console import Console
from rich.table import Table

console = Console()


def load_playlists():
    current_level = 1
    try:
        while True:
            try:
                match current_level:
                    case 1:
                        stored_playlists_raw = client.listplaylists()
                        stored_playlist = []
                        for item in stored_playlists_raw:
                            stored_playlist.append(item["playlist"])
                        pl_table = generate_table(stored_playlist)
                        console.print(pl_table)
                        current_level += 1
                    case 2:
                        user_input = input("Choose: ")
                        handle_input(user_input, stored_playlist)
            except (KeyboardInterrupt, EOFError):
                cs()
                return
    except (KeyboardInterrupt, EOFError):
        cs()
        return


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
