from client import client
from currently_playing import queue
from info_panel import info_panel
from cs import cs
from Colours import colours
import os

from rich import box
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table
from rich.console import Console


console = Console()


def generate_layout():
    # left table
    ltable = Table(
        expand=True,
        row_styles=["", "dim"],
        box=box.SIMPLE_HEAD
    )
    ltable.add_column("#")
    ltable.add_column("Option")

    # middle table
    mtable = Table(
        expand=True,
        row_styles=["", "dim"],
        box=box.SIMPLE_HEAD
    )
    mtable.add_column("#")
    mtable.add_column("Option")

    # right table
    rtable = Table(
        expand=True,
        row_styles=["", "dim"],
        box=box.SIMPLE_HEAD
    )
    rtable.add_column("#")
    rtable.add_column("Option")

    # layout
    layout = Layout()
    layout.split_row(
        Layout(name="left"),
        Layout(name="middle"),
        Layout(name="right")
    )

    # layout size
    _width, _height = os.get_terminal_size()
    console.size = (_width, 14)

    lstrings = [
        "Toggle Repeat",
        "Toggle Random",
        "Toggle Consume",
        "Toggle Single",
        "Toggle Playback",
    ]

    mstrings = [
        "Clear",
        "Crop",
        "Save Current Playlist"
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
            Panel(
                ltable,
                title="Toggles",
                style=colours["yellow"]
            )
        )
    )
    layout["middle"].split(
        Layout(
            Panel(
                mtable,
                title="Playlist",
                style=colours["yellow"]
            )
        )
    )
    layout["right"].split(
        Layout(
            Panel(
                rtable,
                title="Playback",
                style=colours["yellow"]
            )
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
                        info_panel("⟵ Ctrl+c to exit")
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
    confirmation = ""
    status = client.status()
    playlist = queue()

    repeat_tgl = 1 if status["repeat"] == "1" else 0
    random_tgl = 1 if status["random"] == "1" else 0
    consume_tgl = 1 if status["consume"] == "1" else 0
    single_tgl = 1 if status["single"] == "1" else 0

    match access_type:
        case "app":
            while True:
                if len(user_input) <= 11:
                    match user_input:
                        case "1":
                            repeat_tgl ^= 1
                            client.repeat(repeat_tgl)
                            confirmation = "Repeat is on" if repeat_tgl == 1 else "Repeat is off"
                            info_panel(confirmation)
                            break
                        case "2":
                            random_tgl ^= 1
                            client.random(random_tgl)
                            confirmation = "Random mode is on" if random_tgl == 1 else "Random mode is off"
                            info_panel(confirmation)
                            break
                        case "3":
                            consume_tgl ^= 1
                            client.consume(consume_tgl)
                            confirmation = "Consume is on" if consume_tgl == 1 else "Consume is off"
                            info_panel(confirmation)
                            break
                        case "4":
                            single_tgl ^= 1
                            client.single(single_tgl)
                            confirmation = "Single mode is on" if single_tgl == 1 else "Single mode is off"
                            info_panel(confirmation)
                            break
                        case "5":
                            # check if toggle is needed
                            client.pause()
                            info_panel("Playback toggled")
                            break
                        case "6":
                            client.clear()
                            info_panel("Playlist cleared")
                            break
                        case "7":
                            playlist = queue()
                            status = client.status()
                            current_song = playlist["current song"]
                            current_song_progress = status["elapsed"]
                            client.clear()
                            client.add(current_song["file"])
                            client.seek(0, current_song_progress)
                            client.play()
                            break
                        case "8":
                            print('this feature does not work')
                            pl_name = input("Name of playlist: ")
                            client.save(pl_name)
                            break
                        case "9":
                            client.shuffle()
                            info_panel("Shuffled")
                            break
                        case "10":
                            client.previous()
                            info_panel("Playing previous song")
                            break
                        case "11":
                            client.next()
                            info_panel("Playing next song")
                            break
                        case "12":
                            client.stop()
                            info_panel("Playback stopped")
                            break
                        case _:
                            info_panel("Invalid selection")
                            break
                else:
                    info_panel("Invalid selection")
                    break
        case "cli":
            while True:
                match user_input[2]:
                    case "r":
                        repeat_tgl ^= 1
                        client.repeat(repeat_tgl)
                        confirmation = "Repeat is on" if repeat_tgl == 1 else "Repeat is off"
                        info_panel(confirmation)
                        break
                    case "z":
                        random_tgl ^= 1
                        client.random(random_tgl)
                        confirmation = "Random mode is on" if random_tgl == 1 else "Random mode is off"
                        info_panel(confirmation)
                        break
                    case "a":
                        consume_tgl ^= 1
                        client.consume(consume_tgl)
                        confirmation = "Consume is on" if consume_tgl == 1 else "Consume is off"
                        info_panel(confirmation)
                        break
                    case "o":
                        single_tgl ^= 1
                        client.single(single_tgl)
                        confirmation = "Single mode is on" if single_tgl == 1 else "Single mode is off"
                        info_panel(confirmation)
                        break
                    case "t":
                        # check if toggle is needed
                        client.pause()
                        info_panel("Playback toggled")
                        break
                    case "s":
                        client.shuffle()
                        info_panel("Shuffled")
                        break
                    case "p":
                        client.previous()
                        info_panel("Playing previous song")
                        break
                    case "n":
                        client.next()
                        info_panel("Playing next song")
                        break
                    case "x":
                        client.stop()
                        info_panel("Playback stopped")
                        break
                    case "e":
                        client.clear()
                        info_panel("Playlist cleared")
                        break
                    case "c":
                        playlist = queue()
                        status = client.status()
                        current_song = playlist["current song"]
                        current_song_progress = status["elapsed"]
                        client.clear()
                        client.add(current_song["file"])
                        client.seek(0, current_song_progress)
                        client.play()
                        break
                    case _:
                        info_panel("Invalid operation")
                        break
