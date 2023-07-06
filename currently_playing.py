from queue import queue
from client import client
from cs import cs

from rich import box
from rich.layout import Layout
from rich.text import Text
from rich.table import Table
from rich.panel import Panel
from rich.console import Console, Group
from rich.live import Live


console = Console()
layout = Layout()
layout.split_column(
    Layout(name="upper"),
    Layout(name="lower")
)
layout["upper"].size = 15


def currently_playing_layout():
    queue_table = Table(
        expand=True,
        box=box.SIMPLE_HEAD,
        row_styles=["", "dim"]
    )
    queue_table.add_column("Artist")
    queue_table.add_column("#")
    queue_table.add_column("Title")
    queue_table.add_column("Album")
    queue_table.add_column("Length")

    current_song_dictionary = client.currentsong()
    current_song_title = Text(current_song_dictionary["title"], style="b red")
    current_song_album = Text(current_song_dictionary["album"], style="b yellow")
    current_song_artist = Text(current_song_dictionary["artist"], style="b green")
    current_song_title_panel = Panel(Text(current_song_dictionary["title"], style="b red", justify="center"), box=box.SIMPLE_HEAD)
    current_song_album_panel = Panel(Text(current_song_dictionary["album"], style="dim yellow", justify="center"), title="From", box=box.SIMPLE_HEAD)
    current_song_artist_panel = Panel(Text(current_song_dictionary["artist"], style="dim green", justify="center"), title="By", box=box.SIMPLE_HEAD)

    current_status = client.status()
    current_state = ""
    if current_status["state"] == "play":
        current_state = "⏵︎ Playing"
    else:
        current_state = "⏸︎ Paused"

    # current song progress/duration
    current_song_progress = current_status["time"]
    current_song_progress_array = []
    for item in current_song_progress.split(":"):
        current_song_progress_array.append(item)

    current_song_elapsed_seconds = int(current_song_progress_array[0]) % 60
    if current_song_elapsed_seconds < 10:
        current_song_elapsed_seconds = "0" + str(int(current_song_progress_array[0]) % 60)
    current_song_elapsed_minutes = int(int(current_song_progress_array[0]) / 60)

    current_song_duration_seconds = int(current_song_progress_array[1]) % 60
    if current_song_duration_seconds < 10:
        current_song_duration_seconds = "0" + str(int(current_song_progress_array[1]) % 60)
    current_song_duration_minutes = int(int(current_song_progress_array[1]) / 60)
    # --

    # playlist option strings
    repeat = current_status["repeat"]
    repeat_string = ""
    random = current_status["random"]
    random_string = ""
    consume = current_status["consume"]
    consume_string = ""
    single = current_status["single"]
    single_string = ""

    match repeat:
        case "0":
            repeat_string = "-"
        case "1":
            repeat_string = "⥁"

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

    playlist_settings_string = f"\[{repeat_string}{random_string}{consume_string}{single_string}]"
    # --

    current_song_panel_subtitle = f"{playlist_settings_string} {current_song_elapsed_minutes}:{current_song_elapsed_seconds}/{current_song_duration_minutes}:{current_song_duration_seconds}"

    panel_group = Group(
        current_song_title_panel,
        current_song_album_panel,
        current_song_artist_panel
    )
    display_index = 1
    playlist = queue()

    for item in playlist:
        if item["title"] == current_song_dictionary["title"]:
            # queue_table.add_row(Text(str(display_index), style="b yellow"), current_song_title, current_song_album, current_song_artist)
            queue_table.add_row(current_song_artist, Text(str(display_index), style="b cyan"), current_song_title, current_song_album)
        else:
            # queue_table.add_row(str(display_index), item["title"], item["album"], item["artist"])
            queue_table.add_row(item["artist"], Text(str(display_index), style="dim"), item["title"], item["album"], f"")
            # add time of each song in the queue
        display_index += 1

    layout["upper"].split_row(
        Layout(Panel(panel_group, title=current_state, subtitle=current_song_panel_subtitle, padding=2, style="cyan"))
    )
    layout["lower"].split(
        Layout(Panel(queue_table, title="Up Next", padding=2, style="cyan"))
    )

    return layout


def currently_playing():
    try:
        cs()
        with Live(currently_playing_layout(), refresh_per_second=4) as live:
            while True:
                # time.sleep(0.4)
                live.update(currently_playing_layout())
    except KeyboardInterrupt:
        cs()
        return ""


