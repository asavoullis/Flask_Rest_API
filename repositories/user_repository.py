# user_repository.py
from models import User, Account, db
from datetime import datetime


class UserRepository:
    def create_user(self, user_data):
        # print("Calling create_user method in UserRepository")
        # print(f"User data received: {user_data}")
        
        # Convert date_of_birth to a datetime.date object
        date_of_birth = datetime.strptime(user_data['date_of_birth'], '%d-%m-%Y').date()
        user_data['date_of_birth'] = date_of_birth

        new_user = User(**user_data)
        db.session.add(new_user)
        db.session.commit()
        return new_user


    def get_user_by_id(self, user_id):
        # print(f"Inside get_user_by_id repository with user_id: {user_id}")
        return User.query.get(user_id)


    def get_all_users(self):
        return User.query.all()


    def update_user(self, user_id, user_data):
        user = User.query.get(user_id)
        if user:
            for key, value in user_data.items():
                setattr(user, key, value)
            db.session.commit()
            return user
        return None


    def delete_user(self, user_id):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False


    def activate_user(self, user_id):
        user = User.query.get(user_id)
        if user:
            if user.is_active:
                # User is already active, return appropriate message
                return "User is already active"
            else:
                user.is_active = True
                db.session.commit()
                return "User activated successfully"
        return "User not found"

    def deactivate_user(self, user_id):
        # Query the database for a User object with the given user_id
        user = User.query.get(user_id)
        
        # Check if a user with the given user_id was found
        if user:
            # Check if the user is not active (i.e., the user is already deactivated)
            if not user.is_active:
                # If the user is already deactivated, return a message stating so
                return False, "User is already deactivated"
            else:
                # query the Account table to find any accounts with user_id passed
                accounts = Account.query.filter_by(user_id=user.id).all()
                # if NOT any of those accounts have balance greater than 0:
                if not any(account.balance > 0.0 for account in accounts):
                    # If all accounts have a balance of 0.0, set the user's is_active attribute to False
                    user.is_active = False
                    
                    # Commit the changes made to the user (i.e., the deactivation) to the database
                    db.session.commit()
                    
                    # Return a message stating that the user was successfully deactivated
                    return True, "User deactivated successfully"
                else:
                    print("hello")
                    # If not all of the user's accounts have a balance of 0.0, return a message stating so
                    return False, "Cannot deactivate user with active accounts"
        # If no user with the given user_id was found, return a message stating so
        return False, "User not found"

