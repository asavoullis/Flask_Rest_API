from flask import Blueprint, jsonify, request
from services.user_service import UserService


user_bp = Blueprint('users', __name__)
user_service = UserService()


@user_bp.route('/users', methods=['POST'])
def create_user():
    # print("Received request to create a new user")
    user_data = request.get_json()
    # print(f"Received user data: {user_data}")
    new_user = user_service.create_user(user_data)
    return jsonify(new_user.to_dict()), 201


@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # print(f"Inside get_user function with user_id: {user_id}")
    user = user_service.get_user_by_id(user_id)
    if user:
        # print(f"User found: {user}")
        return jsonify(user.to_dict()), 200
    else:
        # print("User not found")
        return jsonify({'message': 'User not found'}), 404


@user_bp.route('/users', methods=['GET'])
def get_users():
    users = user_service.get_all_users()
    users_data = [user.to_dict() for user in users]
    return jsonify(users_data), 200


@user_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    # print(f"Received PUT request to update user with ID: {user_id}")
    user_data = request.get_json()
    # print(f"Received user data: {user_data}")
    updated_user = user_service.update_user(user_id, user_data)
    if updated_user:
        # print(f"User updated: {updated_user}")
        return jsonify(updated_user.to_dict()), 200
    else:
        # print("User not found")
        return jsonify({'message': 'User not found'}), 404


@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    # print(f"Received DELETE request to delete user with ID: {user_id}")
    deleted = user_service.delete_user(user_id)
    if deleted:
        return jsonify({'message': 'User deleted successfully'}), 200
    else:
        return jsonify({'message': 'User not found'}), 404


@user_bp.route('/users/<int:user_id>/activate', methods=['PUT'])
def activate_user(user_id):
    activated, message = user_service.activate_user(user_id)
    if activated:
        return jsonify({'message': 'User account activated successfully'}), 200
    else:
        return jsonify({'message': message}), 400

@user_bp.route('/users/<int:user_id>/deactivate', methods=['PUT'])
def deactivate_user(user_id):
    deactivated, message = user_service.deactivate_user(user_id)
    if deactivated:
        return jsonify({'message': 'User account deactivated successfully'}), 200
    else:
        return jsonify({'message': message}), 400
    