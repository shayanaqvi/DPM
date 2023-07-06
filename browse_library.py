from cs import cs
from client import client
from Menu import Menu
import time
import random

from rich import box
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

menu = Menu()
console = Console()


def browse_library():
    levels = [0, 1, 2, 3]
    current_level = levels[1]

    while True:
        match current_level:
            case 1:
                cs()
                print("Input 'v' to view subdirectory, 'a' to add to queue, 'b' to go back")
                artist_selection = common_browse_interface("", "directory")
                current_level = handle_cbi_output(levels, current_level, artist_selection[0], artist_selection[1], "directory")
            case 2:
                cs()
                print("Input 'v' to view subdirectory, 'a' to add to queue, 'b' to go back")
                album_selection = common_browse_interface(artist_selection[1], "directory")
                current_level = handle_cbi_output(levels, current_level, album_selection[0], album_selection[1], "directory")
            case 3:
                cs()
                print("Input 'a' to add to queue, 'b' to go back")
                title_selection = common_browse_interface(album_selection[1], "file")
                current_level = handle_cbi_output(levels, current_level, title_selection[0], title_selection[1], "file")
            case _:
                cs()
                return ""


def handle_cbi_output(available_levels: list, current_level, action, media_selection, ls_type):
    if ls_type == "directory":
        match action:
            case "v":
                current_level = available_levels[current_level + 1]
                return current_level
            case "a":
                # print message when added, do this during interface
                # design, maybe in a small box at the bottom?
                client.add(media_selection)
                print("Added")
                return current_level
            case "b":
                current_level = available_levels[current_level - 1]
                return current_level
            case _:
                return current_level
    elif ls_type == "file":
        match action:
            case "v":
                return current_level
            case "a":
                # print message when added, do this during interface
                # design, maybe in a small box at the bottom?
                client.add(media_selection)
                print("Added")
                return current_level
            case "b":
                current_level = available_levels[current_level - 1]
                return current_level
            case _:
                return current_level


def common_browse_interface(directory, type):
    list_table = Table(
        expand=True,
        box=box.SIMPLE_HEAD,
        row_styles=["", "dim"]
    )
    list_table.add_column("#")
    list_table.add_column("Title")
    while True:
        try:
            cs()
            list = menu.list_directory(directory, type)
            list_option_array = []
            display_index = 1

            for item in list:
                list_table.add_row(str(display_index), item)
                display_index += 1

            colours = ["red", "yellow", "cyan", "blue", "magenta"]
            random_colour = random.randint(0, 4)

            list_panel = Panel(list_table, title="Browse Library", style=colours[random_colour])

            console.print(list_panel)

            list_option = input("Choose: ")
            for item in list_option.split(" "):
                list_option_array.append(item)

            if len(list_option_array) > 1:
                list_selection = list[int(list_option_array[1]) - 1]
            else:
                list_selection = 0
            return [list_option_array[0], list_selection]
        except (ValueError, TypeError, IndexError):
            pass
