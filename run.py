import os
from flask import Flask, redirect

app = Flask(__name__)
messages = []

def add_messages(username, message):
    messages.append("{}: {}".format(username, message))


@app.route('/')
def index():
    """Main page with instruction"""
    return "To send a message use /USERNAME/MESSAGE"


@app.route("/<username>")
def user(username):
    """Display chat messages"""
    return "Welcome, {0} - {1}".format(username, messages)



@app.route("/<username>/<message>")
def send_message(username, message):
    """Create a new message and redirectback to the chat page"""
    add_messages(username, message)
    return redirect(message)


app.run(host=os.getenv("IP"), port=os.getenv("PORT"), debug=True)
