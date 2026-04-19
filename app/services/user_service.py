users = [
    {"id": 1, "name": "John", "email": "john@test.com"}
]


def get_user_by_id(user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return None


def add_user(name, email):
    new_id = len(users) + 1
    users.append({
        "id": new_id,
        "name": name,
        "email": email
    })


def delete_user(user_id):
    global users
    users = [u for u in users if u["id"] != user_id]
