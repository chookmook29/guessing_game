import unittest
import random

class test_if_statement(unittest.TestCase):
	def test_statements(self):
		array = {"ALLIGATOR":"alligator.png"}
		current = random.choice(array.keys())
		current_image = array[current]
		self.assertIs(current_image, "alligator.png")
		self.assertIs(current, "ALLIGATOR")
		

if __name__ == '__main__':
    unittest.main()