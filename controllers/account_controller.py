from flask import Blueprint, jsonify, request
from services.account_service import AccountService

account_bp = Blueprint('accounts', __name__)
account_service = AccountService()

@account_bp.route('/accounts', methods=['POST'])
def create_account():
    account_data = request.get_json()
    new_account = account_service.create_account(account_data)
    return jsonify(new_account.to_dict()), 201

@account_bp.route('/accounts/<int:account_id>', methods=['GET'])
def get_account(account_id):
    account = account_service.get_account_by_id(account_id)
    if account:
        return jsonify(account.to_dict()), 200
    else:
        return jsonify({'message': 'Account not found'}), 404

@account_bp.route('/accounts', methods=['GET'])
def get_accounts():
    accounts = account_service.get_all_accounts()
    accounts_data = [account.to_dict() for account in accounts]
    return jsonify(accounts_data), 200

@account_bp.route('/accounts/<int:account_id>', methods=['PUT'])
def update_account(account_id):
    account_data = request.get_json()
    updated_account = account_service.update_account(account_id, account_data)
    if updated_account:
        return jsonify(updated_account.to_dict()), 200
    else:
        return jsonify({'message': 'Account not found'}), 404

@account_bp.route('/accounts/<int:account_id>', methods=['DELETE'])
def delete_account(account_id):
    deleted = account_service.delete_account(account_id)
    if deleted:
        return jsonify({'message': 'Account deleted successfully'}), 200
    else:
        return jsonify({'message': 'Account not found'}), 404

@account_bp.route('/user/<int:user_id>', methods=['GET'])
def get_accounts_by_user_id(user_id):
    return jsonify(account_service.get_accounts_by_user_id(user_id))