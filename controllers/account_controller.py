# controllers/account_controller.py
from flask import Blueprint, jsonify, request
from services.account_service import AccountService
from services.transaction_service import TransactionService


account_bp = Blueprint('accounts', __name__)
account_service = AccountService()
transaction_service = TransactionService()

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




# transactions
@account_bp.route('/accounts/<int:account_id>/deposit', methods=['POST'])
def deposit_into_account(account_id):
    # print(f"Received account_id: {account_id}")  
    deposit_data = request.get_json()
    # print(deposit_data)
    deposit_amount = deposit_data.get('amount')
    if deposit_amount is None or deposit_amount <= 0:
        print("Invalid deposit amount")
        return jsonify({'message': 'Invalid deposit amount'}), 400

    result = account_service.deposit_into_account(account_id, deposit_amount)
    if result:
        account_data, transaction_data = result
        # print(f"Account data: {account_data}")
        # print(f"Transaction data: {transaction_data}")
        return jsonify({
            'account': account_data,
            'transaction': transaction_data
        }), 200
    else:
        print("Deposit failed")
        return jsonify({'message': 'Deposit failed'}), 400


@account_bp.route('/accounts/<int:account_id>/withdraw', methods=['POST'])
def withdraw_from_account(account_id):
    withdraw_data = request.get_json()
    withdraw_amount = withdraw_data.get('amount')
    if withdraw_amount is None or withdraw_amount <= 0:
        return jsonify({'message': 'Invalid withdraw amount'}), 400


    account = account_service.withdraw_from_account(account_id, withdraw_amount)
    if account:
        return jsonify(account.to_dict()), 200
    else:
        return jsonify({'message': 'Withdrawal failed'}), 400


@account_bp.route('/accounts/<int:account_id>/transactions', methods=['GET'])
def get_account_transactions(account_id):
    account = account_service.get_account_by_id(account_id)
    if not account:
        return jsonify({'message': 'Account not found'}), 404

    transactions = transaction_service.get_account_transactions(account_id)
    return jsonify(transactions), 200
