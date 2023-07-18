from currently_playing import queue
from client import client


def crop():
    playlist = queue()
    status = client.status()
    current_song = playlist["current song"]
    current_song_progress = status["elapsed"]
    client.clear()
    client.add(current_song["file"])
    client.seek(0, current_song_progress)
    client.play()
