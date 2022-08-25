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
    all_items, random_items = get_db()
    return render_template("index.html", all_items=all_items, random_items=random_items)


# Add items route
@app.route("/add_items", methods=["POST"])
def add_items():
    return request.form["select_items"]


# Connect db to app
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('gratitude_list.db')
        cursor = db.cursor()
        cursor.execute("SELECT phrase FROM gratitudes")
        all_data = cursor.fetchall()

        # Get the string value
        all_data = [str(val[0]) for val in all_data]

        # Randomly select 3 gratitude
        random_list = all_data.copy()
        random.shuffle(random_list)
        random_list = random_list[:3]

    return all_data, random_list


# Terminate db connection
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


# Boilerplate code (execute code only if the file was run directly, and not imported)
if __name__ == '__main__':
    app.run
