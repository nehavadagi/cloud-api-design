import pytest
import sys
import os
from fastapi.testclient import TestClient

# Fix imports by adding src to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from src.main import app

client = TestClient(app)

@pytest.fixture
def mock_db(monkeypatch):
    test_data = {
        "notes": {
            1: {
                "id": 1,
                "title": "Test Note",
                "content": "Test Content",
                "created_at": "2023-01-01T00:00:00",
                "owner_email": "test@example.com"
            }
        },
        "users": {}
    }
    monkeypatch.setattr("src.app.routes.fake_db", test_data)

def test_get_note(mock_db):
    # Test data should match NoteOut schema exactly
    test_note = {
        "id": 1,
        "title": "Test Note",
        "content": "Test Content",
        "created_at": "2023-01-01T00:00:00",
        "owner_email": "test@example.com"
    }
    
    # Update mock database
    from src.app.routes import fake_db
    fake_db["notes"][1] = test_note
    
    # Make request
    response = client.get("/api/notes/1")
    
    # Verify response
    assert response.status_code == 200
    assert response.json() == test_note

