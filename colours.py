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

	def __init__(self):
		pass

	def generate_random_colour(self):
		key = random.randint(0, 5)
		return str(self.colours[key])
