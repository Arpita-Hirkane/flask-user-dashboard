from flask import Blueprint, jsonify
from app.services.user_service import get_user_by_id

user_bp = Blueprint('user', __name__)


@user_bp.route('/user/<int:user_id>')
def get_user(user_id):
    user = get_user_by_id(user_id)
    return jsonify(user)
