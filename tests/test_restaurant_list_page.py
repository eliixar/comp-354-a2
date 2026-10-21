from app import get_db


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


def test_home_page_returns_html(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.mimetype == "text/html"


def test_home_page_shows_page_title(client):
    html = client.get("/").get_data(as_text=True)

    assert "<title>QuickBite</title>" in html


def test_home_page_shows_every_seeded_restaurant(client):
    html = client.get("/").get_data(as_text=True)

    assert "<li>Dominos: Fresh pizza</li>" in html
    assert "<li>Good Burger: Burgers, fries and shakes</li>" in html
    assert "<li>Yum Sushi: Rolls and Japanese favourites</li>" in html


def test_home_page_shows_one_list_item_per_restaurant(client):
    html = client.get("/").get_data(as_text=True)

    assert html.count("<ul>") == 1
    assert html.count("<li>") == 3


def test_home_page_lists_restaurants_alphabetically(app, client):
    add_restaurant(app, "Aardvark Cafe", "Coffee and pastries")

    html = client.get("/").get_data(as_text=True)
    positions = [html.index(name) for name in ("Aardvark Cafe", "Dominos", "Good Burger", "Yum Sushi")]

    assert positions == sorted(positions)


def test_home_page_shows_newly_added_restaurant(app, client):
    add_restaurant(app, "Taco Town", "Tacos and burritos")

    html = client.get("/").get_data(as_text=True)

    assert "<li>Taco Town: Tacos and burritos</li>" in html
    assert html.count("<li>") == 4


def test_home_page_shows_message_when_no_restaurants(app, client):
    clear_restaurants(app)

    response = client.get("/")
    html = response.get_data(as_text=True)

    assert response.status_code == 200
    assert "No restaurants available" in html
    assert "<ul>" not in html
    assert "<li>" not in html


def test_home_page_hides_empty_message_when_restaurants_exist(client):
    html = client.get("/").get_data(as_text=True)

    assert "No restaurants available" not in html


def test_home_page_escapes_restaurant_text(app, client):
    add_restaurant(app, "<script>alert(1)</script>", "Fish & Chips")

    html = client.get("/").get_data(as_text=True)

    assert "<script>alert(1)</script>" not in html
    assert "&lt;script&gt;alert(1)&lt;/script&gt;" in html
    assert "Fish &amp; Chips" in html
