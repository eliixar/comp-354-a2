import os
import sqlite3

import pytest

from app import BASE_DIR, app as flask_app


@pytest.fixture
def app(tmp_path):
    db_path = tmp_path / "test.db"
    conn = sqlite3.connect(db_path)
    for name in ("schema.sql", "seed.sql"):
        with open(os.path.join(BASE_DIR, "db", name)) as f:
            conn.executescript(f.read())
    conn.close()

    flask_app.config.update(TESTING=True, DATABASE=str(db_path))
    yield flask_app


@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client
