from client import client
from cs import cs

from Tables import Tables

from rich.console import Console


console = Console()
current_level = 1


def handle_input(user_input, list_of_playlists):
    user_input_array = []
    for item in user_input.split(" "):
        user_input_array.append(item)

    match len(user_input_array):
        case 1:
            if user_input_array[0] == "a":
                console.print("Index not supplied")
            else:
                console.print("Invalid operation")
        case 2:
            if user_input_array[0] == "a":
                if user_input_array[1].isdigit():
                    selection = list_of_playlists[int(user_input_array[1]) - 1]
                    client.load(selection)
                elif user_input_array[1] == "":
                    console.print("Index not supplied")
                else:
                    console.print("Invalid option")
            else:
                console.print("Invalid operation")
        case _:
            console.print("Invalid operation")


def pl_browse():
    global current_level
    while True:
        match current_level:
            case 1:
                pl_stored_unprocessed = client.listplaylists()
                pl_stored = []
                for pl in pl_stored_unprocessed:
                    pl_stored.append(pl["playlist"])

                Tables.display_table(pl_stored, "Playlists")
                current_level += 1
            case 2:
                try:
                    user_input_unprocessed = input("➙ ")
                    handle_input(user_input_unprocessed, pl_stored)
                except (KeyboardInterrupt, EOFError):
                    cs()
                    return
