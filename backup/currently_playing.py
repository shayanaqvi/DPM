from client import client

from rich import box
from rich.table import Table
from rich.text import Text
from rich.console import Console
from rich.live import Live


console = Console()


def generate_table():
    table = Table(
        expand=True,
        show_header=False,
        box=box.SIMPLE_HEAD,
        style="dim"
    )
    table.add_column("#")
    table.add_column("Title")
    table.add_column("Album")
    table.add_column("Artist", justify="right")
    table.add_column("Length", justify="right")

    display_index = 1
    try:
        queue_raw = queue()
        current_song = queue_raw["current song"]
        current_song_index = queue_raw["current song index"]
        current_status = queue_raw["current status"]
        playlist = queue_raw["current playlist"]

        current_song_elapsed = current_status["time"]
        current_song_elapsed_array = []
        for item in current_song_elapsed.split(":"):
            current_song_elapsed_array.append(item)

        # everything 75 places ahead of the current song index will be
        # added to the table
        for item in playlist[current_song_index:current_song_index+75]:
            if item["id"] == current_song["id"]:
                table.add_row(
                    Text(
                        "⏵︎ " + str(display_index), style="cyan"
                    ) if current_status["state"] == "play" else Text(
                        "⏸︎ " + str(display_index), style="dim"
                    ),
                    Text(
                        item["title"], style="green reverse bold"
                    ) if current_status["state"] == "play" else Text(
                        item["title"], style="green dim"
                    ),
                    Text(
                        item["album"], style="bold yellow"
                    ) if current_status["state"] == "play" else Text(
                        item["album"], style="yellow dim"
                    ),
                    Text(
                        item["artist"], style="bold red"
                    ) if current_status["state"] == "play" else Text(
                        item["artist"], style="red dim"
                    ),
                    Text(
                        return_duration(item["time"]), style="cyan"
                    ) if current_status["state"] == "play" else Text(
                        return_duration(item["time"]), style="dim"
                    )
                )
                table.add_row(
                    "",
                    Text.assemble(
                        (
                            return_duration(current_song_elapsed_array[0]),
                            "bold green"
                        ) if current_status["state"] == "play" else Text(
                            return_duration(current_song_elapsed_array[0]),
                            "dim green"
                        ),
                        (
                            " / ",
                            "dim green"
                        ),
                        (
                            return_duration(current_song_elapsed_array[1]),
                            "dim green"
                        )
                    ),
                    "",
                    "",
                    ""
                )
            else:
                table.add_row(
                        Text("+" + str(display_index), style="dim"),
                        Text(item["title"], style="dim"),
                        Text(item["album"], style="dim"),
                        Text(item["artist"], style="dim"),
                        Text(return_duration(item["time"]), style="dim")
                    )
            display_index += 1
    except (KeyError):
        table.add_row(
            Text("---", style="dim"),
            Text("Nothing is playing", style="red dim"),
            Text("---", style="dim"),
            Text("---", style="dim"),
            Text("---", style="dim"),
        )

    return table


def return_duration(time):
    # hours
    seconds = int(time) % 60
    minutes = int(int(time) / 60)

    if seconds < 10:
        seconds = f"0{int(time) % 60}"

    return f"{minutes}:{seconds}"


def queue():
    current_playlist = client.playlistinfo()
    current_song = client.currentsong()
    current_song_index = 0
    current_status = client.status()

    current_playlist_array = []
    for title in current_playlist:
        current_playlist_array.append(title)

    for item in current_playlist_array:
        if item["id"] == current_song["id"]:
            current_song_index = current_playlist_array.index(item)

    return {
        "current song": current_song,
        "current song index": current_song_index,
        "current status": current_status,
        "current playlist": current_playlist
    }


def currently_playing():
    try:
        with Live(generate_table(), refresh_per_second=4) as live:
            while True:
                live.update(generate_table())
    except (KeyboardInterrupt, EOFError):
        return
