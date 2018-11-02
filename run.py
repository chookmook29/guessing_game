from flask import Flask, render_template, request, session
import random

app = Flask(__name__)

app.secret_key = 'secret'

@app.route("/")
def index():
	return render_template("index.html", user = "")

@app.route("/", methods = ["POST", "GET"])
def user_display():
	array = ("_ _ _", "_ _ _")
	current = random.choice(array)
	session["current"] = current
	user = request.form["new_user"]
	user_greeting = "Welcome " + request.form["new_user"] + "!"
	session["user_greeting"] = user_greeting
	return render_template("game.html", user_greeting = user_greeting, current = current)

@app.route("/answer/", methods=['POST', "GET"])
def answer():
	answer = request.form["answer"]
	return render_template("game.html", answer = answer, current = session.get("current"), user_greeting = session.get("user_greeting"))
	
