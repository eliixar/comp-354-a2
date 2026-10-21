from flask import Flask, current_app, g
import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "quickbite.db")

app = Flask(__name__)
app.config["DATABASE"] = DB_PATH

# Taken from the official flask tutorial 
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys = ON") # Turn it on everytime a DB connection is established

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

app.teardown_appcontext(close_db) # tells Flask to call that function when cleaning up after the response (from official Flask tutorial)

def get_restaurants():
    return get_db().execute("SELECT * FROM restaurants ORDER BY name;").fetchall() # fetchall() to return a list

@app.route("/")
def home():
    return "QuickBite is running"

if __name__ == "__main__":
    app.run(debug=True)