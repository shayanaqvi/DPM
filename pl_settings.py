from cs import cs
from client import client
from inform import inform_user
from messages import messages
from Tables import Tables

from rich.console import Console


console = Console()


def toggle_settings(client_status, setting_to_toggle):
    repeat_toggle = 1 if client_status["repeat"] == "1" else 0
    random_toggle = 1 if client_status["random"] == "1" else 0
    single_toggle = 1 if client_status["single"] == "1" else 0
    consume_toggle = 1 if client_status["consume"] == "1" else 0

    match setting_to_toggle:
        case "repeat":
            repeat_toggle ^= 1
            client.repeat(repeat_toggle)
            confirmation = "Repeat mode is now on" if repeat_toggle == 1 else "Repeat mode is now off"
            inform_user(confirmation, "affirmative")
        case "random":
            random_toggle ^= 1
            client.random(random_toggle)
            confirmation = "Random mode now is on" if random_toggle == 1 else "Random mode is now off"
            inform_user(confirmation, "affirmative")
        case "single":
            single_toggle ^= 1
            client.single(single_toggle)
            confirmation = "Single mode now is on" if single_toggle == 1 else "Single mode now is off"
            inform_user(confirmation, "affirmative")
        case "consume":
            consume_toggle ^= 1
            client.consume(consume_toggle)
            confirmation = "Consume mode now is on" if consume_toggle == 1 else "Consume mode now is off"
            inform_user(confirmation, "affirmative")


def clear_playlist():
    client.clear()
    inform_user("Playlist has been cleared", "affirmative")


def crop_playlist(temp):
    client_status = client.status()
    playlist = current_playlist(client_status)
    current_song = playlist["current song"]
    current_song_progress = client_status["elapsed"]
    client.clear()
    client.add(current_song["file"])
    client.seek(0, current_song_progress)
    client.play()
    inform_user("Playlist has been cropped", "affirmative")


def shuffle_playlist():
    client.shuffle()
    inform_user("Playlist has been shuffled", "affirmative")


def play_pause(client_status):
    match client_status["state"]:
        case "play" | "pause":
            client.pause()
            confirmation = "Playing" if client_status["state"] == "play" else "Paused"
            inform_user(confirmation, "affirmative")
        case "stop":
            # fix later
            client.play(0)


def stop_playback():
    client.stop()
    inform_user("Playback stopped", "affirmative")


def next_previous(direction):
    match direction:
        case "next":
            client.next()
            inform_user("Playing next track", "affirmative")
        case "prev":
            client.previous()
            inform_user("Playing previous track", "affirmative")


def current_playlist(client_status):
    current_playlist = client.playlistinfo()
    match client_status["state"]:
        case "play" | "pause":
            current_song = client.currentsong()
            current_song_index = 0
            current_playlist_array = []
            for title in current_playlist:
                current_playlist_array.append(title)

            for item in current_playlist_array:
                if item["id"] == current_song["id"]:
                    current_song_index = current_playlist_array.index(item)

            return {
                "current song": current_song,
                "current song index": current_song_index,
                "current playlist": current_playlist
            }
        case "stop":
            return {
                "current song": None,
                "current song index": None,
                "current playlist": current_playlist
            }


def handle_input(user_input, client_status):
    user_input_array = []
    for item in user_input.split(" "):
        user_input_array.append(item)

    match len(user_input_array):
        case 1:
            if user_input_array[0].isdigit():
                match user_input_array[0]:
                    case "1":
                        toggle_settings(client_status, "repeat")
                    case "2":
                        toggle_settings(client_status, "random")
                    case "3":
                        toggle_settings(client_status, "single")
                    case "4":
                        toggle_settings(client_status, "consume")
                    case "5":
                        clear_playlist()
                    case "6":
                        crop_playlist(client_status)
                    case "7":
                        shuffle_playlist()
                    case "8":
                        play_pause(client_status)
                    case "9":
                        stop_playback()
                    case "10":
                        next_previous("next")
                    case "11":
                        next_previous("prev")
                    case _:
                        inform_user(messages["Invalid option"], "error")
            else:
                inform_user(messages["Invalid option"], "error")
        case _:
            inform_user(messages["Invalid option"], "error")


def pl_settings():
    cs()
    current_level = 1
    while True:
        client_status = client.status()
        match current_level:
            case 1:
                pl_options_table_unpopulated = Tables.generate_table(["Playlist Options"])
                pl_options_table = Tables.populate_table(
                    pl_options_table_unpopulated,
                    [
                        "Repeat",
                        "Random",
                        "Single",
                        "Consume",
                        "Clear Playlist",
                        "Crop Playlist",
                        "Shuffle Playlist",
                        "Play/Pause",
                        "Stop Playback",
                        "Next",
                        "Previous",
                    ]
                )
                console.print(pl_options_table)
                current_level += 1
            case 2:
                try:
                    user_input_unprocessed = input("➙ ")
                    handle_input(user_input_unprocessed, client_status)
                except (KeyboardInterrupt, EOFError):
                    cs()
                    return
