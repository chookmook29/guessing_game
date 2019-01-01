"""
This test file has to be placed in main directory
and virtual environment installed & enabled, otherwise it won't work
"""
import os
from flask import url_for
from run import app
import unittest
import json


class FlaskTestCase(unittest.TestCase):

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

if __name__ == '__main__':
	
	unittest.main()