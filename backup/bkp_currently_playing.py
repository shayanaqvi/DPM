from playlist import queue
from client import client
from cs import cs

from rich import box
from rich.layout import Layout
from rich.text import Text
from rich.table import Table
from rich.panel import Panel
from rich.console import Group
from rich.live import Live


def currently_playing_layout():
    """Generate the layout of the currently playing screen"""
    # screen layout definition
    layout = Layout()
    layout.split_row(
        Layout(name="upper"),
        Layout(name="lower")
    )
    layout["upper"].size = 50

    # up next/queue table
    queue_table = Table(
        expand=True,
        box=box.SIMPLE_HEAD,
        row_styles=["", "dim"]
    )
    queue_table.add_column("Artist")
    queue_table.add_column("#", width=4)
    queue_table.add_column("Title")
    queue_table.add_column("Album")
    queue_table.add_column("Length")
    try:
        # current song details, for both the table and the panel at the top
        current_song_dictionary = client.currentsong()
        current_song_title = Text(
                current_song_dictionary["title"],
                style="b red"
        )
        current_song_title_panel = Panel(
            Text(
                current_song_dictionary["title"],
                style="b red",
                justify="center"
            ),
            box=box.SIMPLE_HEAD
        )
        current_song_album = Text(
            current_song_dictionary["album"],
            style="b yellow"
        )
        current_song_album_panel = Panel(
            Text(
                current_song_dictionary["album"],
                style="dim yellow",
                justify="center"
            ),
            title="From",
            box=box.SIMPLE_HEAD
        )
        current_song_artist = Text(
            current_song_dictionary["artist"],
            style="b green"
        )
        current_song_artist_panel = Panel(
            Text(
                current_song_dictionary["artist"],
                style="dim green",
                justify="center"
            ),
            title="By",
            box=box.SIMPLE_HEAD
        )

        # current playback status
        current_status = client.status()
        current_state = "⏵︎ Playing" if current_status['state'] == 'play' else "⏸︎ Paused"

        # current song progress/duration
        current_song_progress = current_status["time"]
        current_song_progress_array = []
        for item in current_song_progress.split(":"):
            current_song_progress_array.append(item)

        # # get time elapsed of current song in minutes:seconds
        current_song_elapsed_seconds = int(current_song_progress_array[0]) % 60
        # # # check if a zero needs to be prepended to seconds
        if current_song_elapsed_seconds < 10:
            current_song_elapsed_seconds = "0" + str(int(
                    current_song_progress_array[0]
                ) % 60)
        current_song_elapsed_minutes = int(int(
                current_song_progress_array[0]
            ) / 60)

        # # get time of duration of current song in minutes:seconds
        current_song_duration_seconds = int(current_song_progress_array[1]) % 60
        # # # check if a zero needs to be prepended to seconds
        if current_song_duration_seconds < 10:
            current_song_duration_seconds = "0" + str(int(
                    current_song_progress_array[1]
                ) % 60)
        current_song_duration_minutes = int(int(
                current_song_progress_array[1]
            ) / 60)

        # get the playlist options and display them as icons
        repeat = current_status["repeat"]
        random = current_status["random"]
        consume = current_status["consume"]
        single = current_status["single"]

        match repeat:
            case "0":
                repeat_string = "-"
            case "1":
                repeat_string = "⭮"

        match random:
            case "0":
                random_string = "-"
            case "1":
                random_string = "⤮"

        match consume:
            case "0":
                consume_string = "-"
            case "1":
                consume_string = "⤚"

        match single:
            case "0":
                single_string = "-"
            case "1":
                single_string = "⤞"
        # # produce string containing all playlist options
        pl_settings_string = (
            f'\[{repeat_string}{random_string}{consume_string}{single_string}]'
        )

        # subtitle of the panel containing current song details
        current_song_subtitle = (
            f'{pl_settings_string} '
            f'{current_song_elapsed_minutes}:{current_song_elapsed_seconds}/'
            f'{current_song_duration_minutes}:{current_song_duration_seconds}'
        )

        # group of the panels needed in the upper layout
        panel_group = Group(
            current_song_title_panel,
            current_song_album_panel,
            current_song_artist_panel
        )

        # index to be inserted into the table
        display_index = 1

        # get the current queue
        playlist = queue()

        # populate the queue_table
        for item in playlist:
            if item["title"] == current_song_dictionary["title"]:
                queue_table.add_row(
                    current_song_artist,
                    Text(str(display_index), style="b cyan"),
                    current_song_title,
                    current_song_album,
                    Text(return_song_duration(item["time"]), style="b blue", justify="right"),
                )
            else:
                queue_table.add_row(
                    item["artist"],
                    Text("+" + str(display_index), style="dim"),
                    item["title"],
                    item["album"],
                    Text(return_song_duration(item["time"]), justify="right"),
                )
            display_index += 1

        # populate the layout
        layout["upper"].split_row(
            Layout(
                Panel(
                    panel_group,
                    title=current_state,
                    subtitle=current_song_subtitle,
                    padding=2,
                    style="blue"
                )
            )
        )
        layout["lower"].split(
            Layout(
                Panel(
                    queue_table,
                    title="Up Next",
                    padding=2,
                    style="blue"
                )
            )
        )
        return layout
    # if the playlist is empty/nothing is playing, this is displayed
    except (KeyError):
        playlist = queue()
        display_index = 1

        for item in playlist:
            queue_table.add_row(
                item["artist"],
                Text(str(display_index), style="dim"),
                item["title"],
                item["album"],
                Text(return_song_duration(item["time"]), justify="right")
            )
            display_index += 1

        layout["upper"].split(
            Layout(
                Panel(
                    Text("Nothing is playing", justify="center"),
                    padding=6,
                    style="cyan"
                )
            )
        )
        layout["lower"].split(
            Panel(
                queue_table,
                padding=2,
                style="cyan"
            )
        )
        return layout


def return_song_duration(something):
    minutes = int(int(something) / 60)
    seconds = int(something) % 60
    if seconds < 10:
        seconds = f"0{int(something) % 60}"
    else:
        pass
    return f"{str(minutes)}:{str(seconds)}"


def currently_playing():
    """Update the layout periodically"""
    # cs()
    while True:
        with Live(currently_playing_layout(), refresh_per_second=4) as live:
            try:
                while True:
                    live.update(currently_playing_layout())
            except (KeyboardInterrupt, EOFError):
                live.stop()
                cs()
                # check for any negative effects later
                # client.close()
                return
