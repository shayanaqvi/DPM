# from client import client
from mpd import MPDClient
from info_panel import info_panel


client = 0
client = MPDClient()
client.connect("localhost", 6600)


def shuffle_library():
    client.clear()
    client.add("")
    client.shuffle()
    client.play()
    info_panel("Shuffled!")
