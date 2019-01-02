"""
This test file has to be placed in main directory
and virtual environment installed & enabled, otherwise it won't work
"""
import os
from flask import url_for
from run import app
import unittest
import json
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

	def test_username_length(self):
		new_user = "AB"
		count = len(new_user)
		if count < 3:
			passed = True
		elif count > 10:
			passed = False
		else:
			passed = False
		self.assertEqual(passed, True) 


	def test_dictionary(self):
		dictionary = {"ALLIGATOR":"alligator.png"}
		current = random.choice(list(dictionary.keys()))
		current_image = dictionary[current]
		self.assertIs(current_image, "alligator.png")
		self.assertIs(current, "ALLIGATOR")

	def test_delete_dict_element(self):
		animals = {"BEAR":"bear.png"}
		del animals["BEAR"]
		if animals == {}:
			check = True
		else:
			check = False
		self.assertEqual(check, True)

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


class FlaskTestCase(unittest.TestCase):

	highscore = {"test":1}

	def setUp(self):#App initialize
		self.app = app.test_client()
		self.app.application.config['SECRET_KEY'] = "secret_word"
		self.app.application.config['SESSION_COOKIE_DOMAIN'] = None
		self.app.application.config["SERVER_NAME"] = "{0} {1}".format(os.environ.get('PORT'), os.environ.get('IP'))
	
	def test_index(self):#Check if app sends GET requests
		with app.app_context():
			response = self.app.get("/")
			self.assertEqual(response.status_code, 200)
			self.assertIn("Enter Name:", str(response.data))
			
	def test_data_post(self):#Check if app sends POST requests
		with app.app_context():
			response = self.app.post("new_user")
			self.assertEqual(response.status_code, 200)

	def test_initial_word(self):#Check if game.html has been created
		with app.app_context():
			response = self.app.get("/game")
			self.assertEqual(response.status_code, 200)

	def test_rules(self):#Check if game.html has been created
		with app.app_context():
			response = self.app.get("/rules", data = dict(user = "test2", score = 2)) 
			self.assertIn("every wrong guess", str(response.data))

	def test_final(self):#Check if game.html has been created
		with app.app_context():
			response = self.app.get("/final", data = dict(highscore="test" , user = "test2", score = 2)) 
			self.assertIn("displayed on top of the page", str(response.data))

if __name__ == '__main__':
	
	unittest.main()