import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session

if os.path.exists("env.py"):
	import env


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY") 
messages = []

"""Add messages to the `messages` list"""
def add_messages(username, message):
    now = datetime.now().strftime("%H:%M:%S")
    messages.append("({}) {}: {}".format(now, username, message))


def get_all_messages():
    """Get all of the messages and separate them with a `br`"""
    return "<br>".join(messages)


@app.route('/', methods = ["GET", "POST"])
def index():
    """Main page with instruction"""

    if request.method == "POST":
        session["username"] = request.form["username"]

    if "username" in session:
        return redirect(session["username"])

    return render_template("index.html")
    


@app.route("/<username>")
def user(username):
    """Display chat messages"""
    return "<h1>Welcome, {0}</h1>{1}".format(username, get_all_messages())



@app.route("/<username>/<message>")
def send_message(username, message):
    """Create a new message and redirectback to the chat page"""
    add_messages(username, message)
    return redirect("/" + username)


app.run(host=os.getenv("IP", "0.0.0.0"), port=os.getenv("PORT", "5000"), debug=True)
