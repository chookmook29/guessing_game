from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", user = "")

@app.route("/", methods = ["POST", "GET"])
def user_display():
    return render_template("game.html", user = "Welcome " + request.form["new_user"] + "!")
