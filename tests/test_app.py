from app import get_restaurants


def test_get_restaurants_returns_seeded_restaurants(app):
    with app.app_context():
        restaurants = [dict(r) for r in get_restaurants()]

    assert restaurants == [
        {"id": 1, "name": "Dominos", "description": "Fresh pizza"},
        {"id": 2, "name": "Good Burger", "description": "Burgers, fries and shakes"},
        {"id": 3, "name": "Yum Sushi", "description": "Rolls and Japanese favourites"},
    ]


def test_home_page_lists_restaurants(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"Dominos: Fresh pizza" in response.data
