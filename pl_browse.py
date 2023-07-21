from client import client
from cs import cs
from inform import inform_user
from messages import messages

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
                inform_user(messages["No index"], "error")
            else:
                inform_user(messages["Invalid option"], "error")
        case 2:
            if user_input_array[0] == "a":
                try:
                    if user_input_array[1].isdigit():
                        selection = list_of_playlists[int(user_input_array[1]) - 1]
                        client.load(selection)
                        inform_user(messages["Added to queue"], "affirmative")
                    elif user_input_array[1] == "":
                        inform_user(messages["No index"], "error")
                    else:
                        inform_user(messages["Invalid option"], "error")
                except (IndexError):
                    inform_user(messages["Invalid index"], "error")
            else:
                inform_user(messages["Invalid option"], "error")
        case _:
            inform_user(messages["Invalid option"], "error")


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
