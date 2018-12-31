import unittest
import random

class test(unittest.TestCase):
	def test_correct(self):
		current = "BADGER"
		guess = "A"
		current_hidden = "?" * len(current)
		new_hidden = ""
		for x in range(len(current)):
			if guess == current[x]:
				new_hidden += guess
			else:
				new_hidden += current_hidden[x]
		current_hidden = new_hidden
		self.assertEqual("?A????", current_hidden)

	def test_wrong(self):
		current = "BADGER"
		guess = "W"
		current_hidden = "?" * len(current)
		new_hidden = ""
		for x in range(len(current)):
			if guess == current[x]:
				new_hidden += guess
			else:
				new_hidden += current_hidden[x]
		current_hidden = new_hidden
		self.assertEqual("??????", current_hidden)

	def test_search_through(self):
		array = ("ALLIGATOR", "BADGER", "BEAR", "BISON", "DEER", "DODO", "FOX", "LYNX", "PORCUPINE", "RHINOCEROS", "WOLF")
		letters = ("X","Y","Z")
		current = random.choice(array)
		guess = random.choice(letters)
		self.assertNotIn(guess, current)

	def test_dictionary(self):
		array = {"ALLIGATOR":"alligator.png"}
		current = random.choice(array.keys())
		current_image = array[current]
		self.assertIs(current_image, "alligator.png")
		self.assertIs(current, "ALLIGATOR")

	def test_empty_dict(self):
		highscore = None
		user = "Joe"
		score = "10"
		if highscore is None:
				highscore = {}
				highscore[user] = score
		self.assertEqual({"Joe":"10"}, highscore)
"""
Check if app creates empty dictionary for highscores when first entry arrives,
even if I declared highscore as empty dictionary during initialization,
Sessions was using type conversion changing its value to None crashing whole app
"""
				


if __name__ == '__main__':
	unittest.main()