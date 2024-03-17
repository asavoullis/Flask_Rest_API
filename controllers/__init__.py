from flask import Blueprint

account_bp = Blueprint('accounts', __name__)
user_bp = Blueprint('users', __name__)

from controllers import account_controller, user_controller