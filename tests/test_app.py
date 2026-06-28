from app import app


def test_homepage_loads():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200


def test_dashboard_title_present():
    client = app.test_client()

    response = client.get("/")

    assert b"DevOps" in response.data

def test_invalid_page_returns_404():
    client = app.test_client()

    response = client.get("/thispagedoesnotexist")

    assert response.status_code == 404