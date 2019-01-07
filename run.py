import os 
from flask import Flask, render_template, request, session
import random
import json

app = Flask(__name__)

app.secret_key = "secret_word"# Password for sessions, which wouldn't work otherwise

SESSION_TYPE = "redis"# Again, needed by sessions to work, redis used as the storage backend because there is a lot of session data
app.config.from_object(__name__)

@app.route("/")
def index():
	message = "Please enter your name."
	return render_template("index.html", message = message)

@app.route("/initial_word", methods = ["POST", "GET"])
def initial_word():
	user = request.form["new_user"]
	count = len(user)# Defensive design, preventing users from creating nicknames with zero, not enough, or too many letters
	if count < 3:
		message_color = "red"# As pointed out by mentor, red colour for warning messages to improve UX
		message = "Your name is too short, please try again."
		return render_template("index.html", message = message, message_color = message_color)# Colour variable sent straight to template, wouldn't work in separate stylesheet css file 
	elif count > 10:
		message_color = "red"
		message = "Your name is too long, please try again."
		return render_template("index.html", message = message, message_color = message_color)
	else:# After checking for user name length, this is the main part of the template's code
		with open('data/animals.json') as json_data:# Dictionary stored in json file to save space in main code, could use separate scripts but app's scope is too small
			animals = json.load(json_data)
		letter_array = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
		session["letter_array"] = letter_array# Array is being stored because it's being used few more times in other templates
		used = "USED: "# "used" and "guess" are variables initially displayed on game's main screen, so they need some initial value, otherwise app would display blank spaces
		guess = "?"
		session["used"] = used
		score = 0# Resets game's elements so previous users can't continue same game after losing
		attempts = 8
		session["score"] = score
		session["attempts"] = attempts
		current = random.choice(list(animals.keys()))# "list" method added because Python 3 would interpret it incorrectly (not as a list)
		current_image = animals[current]
		del animals[current] # This feature prevents current question from reappearing later in the game
		session["animals"] = animals
		current_hidden = "ˍ" * len(current)# Special narrower underscore used from expanded UTF-8 set, standard one causing problems (would merge and create continuous line)
		""" Name "current_hidden" means it has letters concealed behind "ˍ", not hidden from view in general, it can be potentially misleading. 
			Variable "current" is the hidden word in a true meaning.
		"""
		session["current"] = current
		session["current_image"] = current_image
		session["current_hidden"] = current_hidden
		user_greeting = "Welcome " + user + "!"
		""" "user_greeting" differs from "user", as it's whole sentence pasted into main game screen, I couldn't just use "user" variable as the sentence changes to "TRY NOW" and "CORRECT" after
			certain actions, so I had to create different, more specific variable than just "user".
		"""
		session["user_greeting"] = user_greeting
		session["user"] = user
		return render_template("game.html", user_greeting = user_greeting, current = current_hidden, current_image = current_image, user = user, letter_array = letter_array, attempts = attempts, score =  score, used = used, guess = guess)

@app.route("/user_guess", methods=['POST', "GET"])
def user_guess():
	letter_array = session.get("letter_array")
	guess = request.form["guess"]
	guess = guess.upper()
	used = session.get("used")
	used += guess
	session["used"] = used
	current_hidden = session.get("current_hidden")
	current = session.get("current")
	current_image = session.get("current_image")
	user = session.get("user")
	score = session.get("score")
	attempts =  session.get("attempts")
	if guess in current and guess not in current_hidden:# "guess not in current_hidden" condition prevents from guessing same exact letter twice (defensive design)
		new_hidden = ""# Initialized as empty otherwise wouldn't be possible to add value
		for x in range(len(current)):# Searching through and adding to displayed word
			if guess == current[x]:
				new_hidden += guess
			else:
				new_hidden += current_hidden[x]
		current_hidden = new_hidden
		session["current_hidden"] = current_hidden
		if current_hidden == current:# What happens when the whole word is guessed correctly
			score += 1
			attempts = 8
			session["current"] = current
			session["score"] = score
			session["attempts"] = attempts
			return render_template("correct.html", guess = guess, current = current, current_image = current_image, user_greeting = "TRY NOW!", used = used, score = score, user = user, letter_array = letter_array, attempts = attempts)
		else: # Correct guess but not the whole word yet
			return render_template("game.html", guess = guess, current = current_hidden, current_image = current_image, user_greeting = "CORRECT!", used = used, score = score, user = user, letter_array = letter_array, attempts = attempts)
	else:# Wrong guess or same letter again
		attempts -= 1
		if attempts == 0:# If down to zero attempts
			highscore = session.get("highscore")
			user = session.get("user")
			score = session.get("score")
			highscore = session.get("highscore")
			""" Main reason of using if statements below is that even if highscore was declared as empty dictionary
				somewhere at the beginning, it would always get value of NoneType every time its value is requested, so thats why it has to be 
				declared as an empty dictionary here again every new game starts. Possible flask-sessions bug or limitation?"""
			if highscore is None:
				highscore = {}
				highscore[user] = score
				session["highscore"] = highscore
				final_message = "GAME OVER!"
				return render_template("final.html", highscore = highscore, user = user, score = score, final_message = final_message)	
			else:
				highscore[user] = score
				session["highscore"] = highscore
				final_message = "GAME OVER!"
				return render_template("final.html", highscore = highscore, user = user, score = score, final_message = final_message)
		else:
			session["attempts"] = attempts
			return render_template("game.html", guess = guess, current = current_hidden, current_image = current_image, user_greeting = "WRONG!", used = used, score = score, user = user, letter_array = letter_array,  attempts = attempts)

@app.route("/next_word", methods=['POST', "GET"])
def next_word():
	letter_array = session.get("letter_array")
	current_hidden = session.get("current_hidden")
	current = session.get("current")
	guess = "?"
	user = session.get("user")
	score = session.get("score")
	attempts = session.get("attempts")
	animals = session.get("animals")
	if animals == {}:# If dictionary becomes empty, it means player completed the game
		user = session.get("user")
		score = session.get("score")
		highscore = session.get("highscore")
		top_user = session.get("user")
		score = session.get("score")
		highscore = session.get("highscore")
		if highscore is None:
			highscore = {}
			highscore[top_user] = score
			session["highscore"] = highscore
			final_message = "Congratulations!"
			return render_template("final.html", highscore = highscore, user = user, score = score, final_message = final_message)	
		else:
			highscore[top_user] = score
			session["highscore"] = highscore
			final_message = "Congratulations!"
			return render_template("final.html", highscore = highscore, user = user, score = score, final_message = final_message)	
	else:
		current = random.choice(list(animals.keys()))
		current_image = animals[current]
		del animals[current]
		session["animals"] = animals
		current_hidden = "ˍ" * len(current)
		session["current"] = current
		session["current_image"] = current_image
		session["current_hidden"] = current_hidden
		used = "USED: "
		session["used"] = used
		session["score"] = score
		session["attempts"] = attempts
		return render_template("game.html", guess = guess, current = current_hidden, current_image = current_image, user_greeting = "TRY NOW!", used = used, score = score, user = user, letter_array = letter_array,  attempts = attempts)

@app.route("/check", methods=['POST', "GET"])# Option that still make it possible to come back to main game
def check():
	user = session.get("user")
	score = session.get("score")
	highscore = session.get("highscore")
	top_user = session.get("user")
	score = session.get("score")
	highscore = session.get("highscore")
	if highscore is None:
		highscore = {}
		highscore[top_user] = score
		session["highscore"] = highscore
		return render_template("score.html", highscore = highscore, user = user, score = score)	
	else:
		highscore[top_user] = score
		session["highscore"] = highscore
		return render_template("score.html", highscore = highscore, user = user, score = score)

@app.route("/back", methods=['POST', "GET"])# Keeps all the crucial variables to make continuing game possible after choosing option in the menu
def back():
	letter_array = session.get("letter_array")
	current_hidden = session.get("current_hidden")
	current = session.get("current")
	current_image = session.get("current_image")
	user = session.get("user")
	score = session.get("score")
	attempts =  session.get("attempts")
	used = session.get("used")
	guess = "?"
	return render_template("game.html", guess = guess, current = current_hidden, current_image = current_image, user_greeting = "TRY NOW!", used = used, score = score, user = user, letter_array = letter_array,  attempts = attempts)

@app.route("/rules")
def rules():
	user = session.get("user")
	score = session.get("score")
	return render_template("rules.html", user = user, score = score)

@app.errorhandler(410)
@app.errorhandler(404)
@app.errorhandler(500)
def error_display(self):
	return render_template("error.html")

if __name__ == '__main__':
	app.run(host=os.environ.get('IP'),
			port=int(os.environ.get('PORT')),
			debug=False)
