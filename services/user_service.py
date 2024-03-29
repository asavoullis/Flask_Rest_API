from repositories.user_repository import UserRepository

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def create_user(self, user_data):
        # print("Calling create_user method in UserService")
        # print(f"User data received: {user_data}")
        return self.user_repository.create_user(user_data)

    def get_user_by_id(self, user_id):
        return self.user_repository.get_user_by_id(user_id)

    def get_all_users(self):
        return self.user_repository.get_all_users()

    def update_user(self, user_id, user_data):
        return self.user_repository.update_user(user_id, user_data)