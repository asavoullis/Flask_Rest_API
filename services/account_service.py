# services/account_service.py
from models import db
from repositories.account_repository import AccountRepository
from services.transaction_service import TransactionService

class AccountService:
    def __init__(self):
        self.account_repository = AccountRepository()
        self.transaction_service = TransactionService()

    def create_account(self, account_data):
        return self.account_repository.create_account(account_data)

    def get_account_by_id(self, account_id):
        return self.account_repository.get_account_by_id(account_id)

    def get_all_accounts(self):
        return self.account_repository.get_all_accounts()

    def update_account(self, account_id, account_data):
        return self.account_repository.update_account(account_id, account_data)

    def delete_account(self, account_id):
        return self.account_repository.delete_account(account_id)
    
    def get_accounts_by_user_id(self, user_id):
        accounts = self.account_repository.get_accounts_by_user_id(user_id)
        return [account.to_dict() for account in accounts]


# transactions
    def deposit_into_account(self, account_id, amount):
        # print(f"Deposit into account with ID: {account_id}, Amount: {amount}")
        account = self.get_account_by_id(account_id)
        if account:
            account.balance += amount
            db.session.commit()
            # print(f"Account balance updated: {account.balance}")
            transaction_data = {
                'account_id': account_id,
                'transaction_type': 'deposit',
                'amount': amount
            }
            transaction = self.transaction_service.create_transaction(transaction_data)
            # print(f"Transaction created: {transaction}")
            return account.to_dict(), transaction.to_dict()
        else:
            print(f"Account with ID {account_id} not found")
        return None


    def withdraw_from_account(self, account_id, amount):
        account = self.get_account_by_id(account_id)
        if account and account.balance >= amount:
            account.balance -= amount
            db.session.commit()
            transaction_data = {
                'account_id': account_id,
                'transaction_type': 'withdrawal',
                'amount': amount
            }
            self.transaction_service.create_transaction(transaction_data)
            return account
        return None

    def activate_account(self, account_id):
        result = self.account_repository.activate_account(account_id)
        if result == "Account activated successfully":
            return True, result
        else:
            return False, result

    def deactivate_account(self, account_id):
        result = self.account_repository.deactivate_account(account_id)
        if result == "Account deactivated successfully":
            return True, result
        else:
            return False, result