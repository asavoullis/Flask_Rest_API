from models import Account, db

class AccountRepository:
    def create_account(self, account_data):
        new_account = Account(**account_data)
        db.session.add(new_account)
        db.session.commit()
        return new_account

    def get_account_by_id(self, account_id):
        return Account.query.get(account_id)

    def get_all_accounts(self):
        return Account.query.all()

    def update_account(self, account_id, account_data):
        account = Account.query.get(account_id)
        if account:
            for key, value in account_data.items():
                setattr(account, key, value)
            db.session.commit()
            return account
        return None

    def delete_account(self, account_id):
        account = Account.query.get(account_id)
        if account:
            db.session.delete(account)
            db.session.commit()
            return True
        return False