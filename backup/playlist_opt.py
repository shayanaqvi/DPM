from client import client
from currently_playing import queue
from info_panel import info_panel
from cs import cs
from load_playlist import load_playlists
from Colours import colours
import os

from rich import box
from rich.layout import Layout
from rich.table import Table
from rich.console import Console


console = Console()


def generate_layout():
    # left table
    ltable = Table(
        expand=True,
        box=box.SIMPLE,
        style=colours["accent1"]
    )
    ltable.add_column(
        "#",
        style=colours["accent1"],
        header_style=colours["accent1"]
    )
    ltable.add_column(
        "Toggles",
        header_style=colours["accent1"]
    )

    # middle table
    mtable = Table(
        expand=True,
        box=box.SIMPLE,
        style=colours["accent1"]
    )
    mtable.add_column("#", style=colours["accent1"], header_style=colours["accent1"])
    mtable.add_column(
        "Playlist",
        header_style=colours["accent1"]
    )

    # right table
    rtable = Table(
        expand=True,
        box=box.SIMPLE,
        style=colours["accent1"]
    )
    rtable.add_column("#", style=colours["accent1"], header_style=colours["accent1"])
    rtable.add_column(
        "Playback",
        header_style=colours["accent1"]
    )
    # layout
    layout = Layout()
    layout.split_row(
        Layout(name="left"),
        Layout(name="middle"),
        Layout(name="right")
    )

    # layout size
    _width, _height = os.get_terminal_size()
    console.size = (_width, 9)

    lstrings = [
        "Toggle Repeat",
        "Toggle Random",
        "Toggle Consume",
        "Toggle Single",
        "Toggle Playback",
    ]

    mstrings = [
        "Load Playlist",
        "Save Playlist",
        "Clear",
        "Crop",
    ]

    rstrings = [
        "Shuffle Playlist",
        "Previous Track",
        "Next Track",
        "Stop Playback",
    ]

    display_index = 1
    for item in lstrings:
        ltable.add_row(str(display_index), item)
        display_index += 1

    for item in mstrings:
        mtable.add_row(str(display_index), item)
        display_index += 1

    for item in rstrings:
        rtable.add_row(str(display_index), item)
        display_index += 1

    # add to layout
    layout["left"].split(
        Layout(
                ltable,
        )
    )
    layout["middle"].split(
        Layout(
                mtable,
        )
    )
    layout["right"].split(
        Layout(
                rtable,
        )
    )

    return layout


def playlist_options(cli_arguments):
    current_level = 1
    match len(cli_arguments):
        case 2:
            cs()
            while True:
                match current_level:
                    case 1:
                        console.print(generate_layout())
                        info_panel("⟵ Ctrl+c to exit", "information")
                        current_level += 1
                    case 2:
                        try:
                            operation = input("Do: ")
                            handle_input(operation, "app")
                        except (KeyboardInterrupt, EOFError):
                            cs()
                            return
                    case _:
                        pass
        case 3:
            handle_input(cli_arguments, "cli")


def handle_input(user_input, access_type):
    status = client.status()
    toggles = {
        "repeat": 1 if status["repeat"] == "1" else 0,
        "random": 1 if status["random"] == "1" else 0,
        "consume": 1 if status["consume"] == "1" else 0,
        "single": 1 if status["single"] == "1" else 0,
    }
    keys_app = {
        "1": toggles["repeat"],
        "2": toggles["random"],
        "3": toggles["consume"],
        "4": toggles["single"],
    }

    match access_type:
        case "app":
            while True:
                if len(user_input) <= 11:
                    match user_input:
                        
        case "cli":
            pass


def toggle_setting(toggle, operation_type):
    toggle ^= 1
    match operation_type:
        case "repeat":
            client.repeat(toggle)
            confirmation = "Repeat is on" if toggle == 1 else "Repeat is off"
            info_panel(confirmation, "affirmative")
        case "random":
            client.random(toggle)
            confirmation = "Random mode is on" if toggle == 1 else "Random mode is off"
            info_panel(confirmation, "affirmative")
        case "consume":
            client.consume(toggle)
            confirmation = "Consume mode is on" if toggle == 1 else "Consume mode is off"
            info_panel(confirmation, "affirmative")
        case "single":
            client.single(toggle)
            confirmation = "Single mode is on" if toggle == 1 else "Single mode is off"
            info_panel(confirmation, "affirmative")
