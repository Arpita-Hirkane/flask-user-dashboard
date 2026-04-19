from app.services.user_service import get_user_by_id


def test_get_user_success():
    user = get_user_by_id(1)

    assert user['name'] == 'John'
    assert user['email'] == 'john@test.com'
