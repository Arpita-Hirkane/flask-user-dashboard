from app.main import app
import pytest


@pytest.fixture
def client():
    app.testing = True
    return app.test_client()


def test_get_user_route(client, monkeypatch):
    def mock_user(id):
        return {'id': 1, 'name': 'John', 'email': 'john@test.com'}

    monkeypatch.setattr(
        'app.routes.user_routes.get_user_by_id',
        mock_user
    )

    response = client.get('/user/1')

    assert response.status_code == 200
