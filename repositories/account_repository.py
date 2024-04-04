# account_repository.py
from models import Account, User, db

class AccountRepository:
    def create_account(self, account_data):
        user = User.query.get(account_data['user_id'])
        if user:
            if user.is_active:
                new_account = Account(**account_data)
                db.session.add(new_account)
                db.session.commit()
                return new_account
            else:
                return None, "User is not active"
        else:
            return None, "User not found"

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
    
    def get_accounts_by_user_id(self, user_id):
        return Account.query.filter_by(user_id=user_id).all()



    def activate_account(self, account_id):
        account = Account.query.get(account_id)
        if account:
            if account.is_active:
                return "Account is already active"
            else:
                account.is_active = True
                db.session.commit()
                return "Account activated successfully"
        return "Account not found"

    def deactivate_account(self, account_id):
        account = Account.query.get(account_id)
        if account:
            if not account.is_active:
                return "Account is already deactivated"
            else:
                account.is_active = False
                db.session.commit()
                return "Account deactivated successfully"
        return "Account not found"