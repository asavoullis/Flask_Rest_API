# services/transaction_service.py
from repositories.transaction_repository import TransactionRepository

class TransactionService:
    def __init__(self):
        self.transaction_repository = TransactionRepository()

    def create_transaction(self, transaction_data):
        return self.transaction_repository.create_transaction(transaction_data)

    def get_account_transactions(self, account_id):
        transactions = self.transaction_repository.get_account_transactions(account_id)
        return [transaction.to_dict() for transaction in transactions]