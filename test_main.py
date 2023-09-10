from fastapi.testclient import TestClient

from Models.ClassifiedTicket import ClassifiedTicketModel
from main import app

client = TestClient(app)
base_categories = ['New Member', 'Terminated Member', 'Problem']


def test_classify_ticket():
    title = "I can't log in to my account"
    desc = "I can't log in to my account. I have tried resetting my password but it doesn't work. Please help."

    response = client.post(
        "/classify_ticket",
        json={
            "title": title,
            "description": desc,
            "category": base_categories
        }
    )
    assert response.status_code == 200
    json_response: ClassifiedTicketModel = response.json()
    assert json_response.title == title
    assert json_response.description == desc
    assert sum(json_response.classification.values()) == 1.0
    assert json_response.classification['Service Request'] > 0.5
