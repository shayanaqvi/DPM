import random


class ReturnColour():
    colours = [
        "red",
        "green",
        "yellow",
        "blue",
        "magenta",
        "cyan"
    ]

    def generate_random_colour(self):
        """Generate a random colour"""
        key = random.randint(0, 5)
        return str(self.colours[key])
