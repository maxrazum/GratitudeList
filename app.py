from flask import Flask, session, render_template, request, g

import os
import sqlite3
import random


# Configure application
app = Flask(__name__)

# Configure session
app.secret_key = os.urandom(24)

# Main route
@app.route("/")
def index():
    return "<h1>Hello, world</h1>"


# Connect db to app
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('gratitude_list.db')
    return db


# Terminate db connection
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Boilerplate code (execute code only if the file was run directly, and not imported)
if __name__ == '__main__':
    app.run

