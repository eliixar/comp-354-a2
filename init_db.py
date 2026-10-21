import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "quickbite.db")
SCHEMA_PATH = os.path.join(BASE_DIR, "db", "schema.sql")
SEED_PATH = os.path.join(BASE_DIR, "db", "seed.sql")

# Remove the existing database to start fresh and avoid duplicate seed data
if os.path.exists(DB_PATH):
    os.remove(DB_PATH)

conn = sqlite3.connect(DB_PATH)

with open(SCHEMA_PATH) as f:
    conn.executescript(f.read())
with open(SEED_PATH) as f:
    conn.executescript(f.read())

conn.commit()
conn.close()
print("Database created: quickbite.db")