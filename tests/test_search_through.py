import unittest
import random

class test_if_statement(unittest.TestCase):
	def test_statements(self):
		array = ("ALLIGATOR", "BADGER", "BEAR", "BISON", "DEER", "DODO", "FOX", "LYNX", "PORCUPINE", "RHINOCEROS", "WOLF")
		letters = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
		current = random.choice(array)
		guess = random.choice(letters)
		self.assertIn(guess, current)
		self.assertNotIn(guess, current)
		

if __name__ == '__main__':
    unittest.main()