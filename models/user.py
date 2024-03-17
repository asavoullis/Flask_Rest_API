from models.extensions import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    telephone_number = db.Column(db.String(20), nullable=False)
    country_code = db.Column(db.String(5), nullable=False)
    post_code = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    date_of_birth = db.Column(db.Date, nullable=False)
    accounts = db.relationship('Account', backref='user', lazy='dynamic')

    def __repr__(self):
        return f'<User {self.username}>'