from repositories.account_repository import AccountRepository

class AccountService:
    def __init__(self):
        self.account_repository = AccountRepository()

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