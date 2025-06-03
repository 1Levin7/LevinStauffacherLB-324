from app import app, entries
import pytest


@pytest.fixture()
def client():
    app.config["TESTING"] = True
    client = app.test_client()
    entries.clear()
    yield client


def test_add_entry(client):
    with client.session_transaction() as sess:
        sess["logged_in"] = True
    response = client.post("/add_entry", data={"content": "Test Entry"})
    assert response.status_code == 302
    assert entries[0].content == "Test Entry"


def test_add_entry_with_mood(client):
    with client.session_transaction() as sess:
        sess["logged_in"] = True
    response = client.post(
        "/add_entry",
        data={
            "content": "Test mit Stimmung",
            "mood_score": "8",
            "mood_keyword": "Sternenmut",
        },
    )
    assert response.status_code == 302
    assert entries[0].mood_score == 8
    assert entries[0].mood_keyword == "Sternenmut"
