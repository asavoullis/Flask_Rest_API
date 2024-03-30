from models import User, db
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
        user = User.query.get(user_id)
        if user:
            if not user.is_active:
                # User is already deactivated, return appropriate message
                return "User is already deactivated"
            else:
                user.is_active = False
                db.session.commit()
                return "User deactivated successfully"
        return "User not found"
