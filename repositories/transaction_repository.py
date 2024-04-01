# repositories/transaction_repository.py
from models.transaction import Transaction
from models.extensions import db

class TransactionRepository:
    def create_transaction(self, transaction_data):
        new_transaction = Transaction(**transaction_data)
        db.session.add(new_transaction)
        db.session.commit()
        return new_transaction

    def get_account_transactions(self, account_id):
        return Transaction.query.filter_by(account_id=account_id).all()