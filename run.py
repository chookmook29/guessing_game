import os
from flask import Flask, render_template, request, session
import random

app = Flask(__name__)

app.secret_key = "secret_word"

SESSION_TYPE = "redis"
app.config.from_object(__name__)

@app.route("/")
def index():
	return render_template("index.html", user = "")

@app.route("/", methods = ["POST", "GET"])
def user_display():
	array = ("ALLIGATOR", "BADGER", "BEAR", "BISON", "DEER", "DODO", "FOX", "LYNX", "PORCUPINE", "RHINOCEROS", "WOLF", "EAGLE", "GIRAFFE", "TURTLE", "PANDA", "HAWK", "DOLPHIN", "OWL", "LEOPARD")
	session["array"] = array
	letter_array = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
	used = "USED: "
	session["used"] = used
	score = 0
	session["score"] = score
	current = random.choice(array)
	current_hidden = "?" * len(current)
	session["current"] = current
	session["current_hidden"] = current_hidden
	user = request.form["new_user"]
	session["user"] = user
	user_greeting = "Welcome " + user + "!"
	session["user_greeting"] = user_greeting
	return render_template("game.html", user_greeting = user_greeting, current = current_hidden, letter_array = letter_array)

@app.route("/guess/", methods=['POST', "GET"])
def guess():
	letter_array = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
	guess = request.form["guess"]
	guess = guess.upper()
	used = session.get("used")
	used += guess
	session["used"] = used
	current_hidden = session.get("current_hidden")
	current = session.get("current")
	user = session.get("user")
	user += ": "
	score = session.get("score")
	if guess in current and current_hidden != current:
		score += 1
		session["score"] = score
		new_hidden = ""
		for x in range(len(current)):
			if guess == current[x]:
				new_hidden += guess
			else:
				new_hidden += current_hidden[x]
		current_hidden = new_hidden
		session["current_hidden"] = current_hidden
		if current_hidden == current:
			array = session.get("array")
			current = random.choice(array)
			current_hidden = "?" * len(current)
			session["current"] = current
			session["current_hidden"] = current_hidden
			used = "USED: "
			session["used"] = used
			session["score"] = score
			return render_template("game.html", guess = guess, current = current_hidden, user_greeting = "TRY NOW!", used = used, score = score, user = user, letter_array = letter_array)
		else:
			return render_template("game.html", guess = guess, current = current_hidden, user_greeting = "CORRECT!", used = used, score = score, user = user, letter_array = letter_array)
	elif current_hidden != current:
		if score == 0:
			session["score"] = score
			return render_template("game.html", guess = guess, current = current_hidden, user_greeting = "WRONG!", used = used, score = score, user = user, letter_array = letter_array)
		else:
			score -= 1
			session["score"] = score
			return render_template("game.html", guess = guess, current = current_hidden, user_greeting = "WRONG!", used = used, score = score, user = user, letter_array = letter_array)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False)
