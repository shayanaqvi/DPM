from client import client
from inform import inform_user


def shuffle():
    client.clear()
    client.add("")
    client.shuffle()
    client.play(0)
    inform_user("Library has been shuffled", "affirmative")
