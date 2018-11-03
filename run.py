from flask import Flask, render_template, request, session
import random

app = Flask(__name__)

app.secret_key = 'secret'

@app.route("/")
def index():
	return render_template("index.html", user = "")

@app.route("/", methods = ["POST", "GET"])
def user_display():
	array = ("DOG", "CAT")
	used = []
	score = 0
	session["score"] = score
	session["used"] = used
	current = random.choice(array)
	current_hidden = "?" * len(current)
	session["current"] = current
	session["current_hidden"] = current_hidden
	user = request.form["new_user"]
	session["user"] = user
	user_greeting = "Welcome " + user + "!"
	session["user_greeting"] = user_greeting
	session["user"] = user
	return render_template("game.html", user_greeting = user_greeting, current = current_hidden)

@app.route("/guess/", methods=['POST', "GET"])
def guess():
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
	if guess in current:
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
		return render_template("game.html", guess = guess, current = current_hidden, user_greeting = "CORRECT!", used = used, score = score, user = user)
	else:
		if score == 0:
			session["score"] = score
			return render_template("game.html", guess = guess, current = current_hidden, user_greeting = "WRONG!", used = used, score = score, user = user)
		else:
			score -= 1
			session["score"] = score
			return render_template("game.html", guess = guess, current = current_hidden, user_greeting = "WRONG!", used = used, score = score, user = user)

