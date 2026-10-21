import sqlite3

import pytest

from app import get_db, get_restaurants


def clear_restaurants(app):
    with app.app_context():
        db = get_db()
        db.execute("DELETE FROM menu_items")
        db.execute("DELETE FROM restaurants")
        db.commit()


def add_restaurant(app, name, description):
    with app.app_context():
        db = get_db()
        db.execute(
            "INSERT INTO restaurants (name, description) VALUES (?, ?)",
            (name, description),
        )
        db.commit()


def test_get_restaurants_returns_a_list(app):
    with app.app_context():
        restaurants = get_restaurants()

    assert isinstance(restaurants, list)
    assert len(restaurants) == 3


def test_get_restaurants_rows_are_accessible_by_column_name(app):
    with app.app_context():
        first = get_restaurants()[0]

    assert first["id"] == 1
    assert first["name"] == "Dominos"
    assert first["description"] == "Fresh pizza"


def test_get_restaurants_is_sorted_by_name_not_insertion_order(app):
    add_restaurant(app, "Aardvark Cafe", "Coffee and pastries")
    add_restaurant(app, "Mango Grill", "Grilled skewers")

    with app.app_context():
        names = [r["name"] for r in get_restaurants()]

    assert names == ["Aardvark Cafe", "Dominos", "Good Burger", "Mango Grill", "Yum Sushi"]


def test_get_restaurants_returns_empty_list_when_no_restaurants(app):
    clear_restaurants(app)

    with app.app_context():
        assert get_restaurants() == []


def test_get_restaurants_includes_restaurant_without_description(app):
    add_restaurant(app, "Plain Place", None)

    with app.app_context():
        restaurants = {r["name"]: r["description"] for r in get_restaurants()}

    assert "Plain Place" in restaurants
    assert restaurants["Plain Place"] is None


def test_get_db_reuses_connection_within_app_context(app):
    with app.app_context():
        assert get_db() is get_db()


def test_get_db_uses_configured_database(app):
    with app.app_context():
        db_file = get_db().execute("PRAGMA database_list").fetchone()["file"]

    assert db_file == app.config["DATABASE"]


def test_get_db_enables_foreign_keys(app):
    with app.app_context():
        db = get_db()
        assert db.execute("PRAGMA foreign_keys").fetchone()[0] == 1

        with pytest.raises(sqlite3.IntegrityError):
            db.execute(
                "INSERT INTO menu_items (restaurant_id, name, price) VALUES (?, ?, ?)",
                (999, "Ghost Item", 1.00),
            )


def test_connection_is_closed_after_app_context_ends(app):
    with app.app_context():
        db = get_db()

    with pytest.raises(sqlite3.ProgrammingError):
        db.execute("SELECT 1")


def test_new_app_context_gets_new_connection(app):
    with app.app_context():
        first = get_db()

    with app.app_context():
        second = get_db()

    assert first is not second
