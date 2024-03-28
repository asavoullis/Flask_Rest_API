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
    registration_date = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<User {self.username}>'

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'first_name': self.first_name,
            'surname': self.surname,
            'address': self.address,
            'telephone_number': self.telephone_number,
            'country_code': self.country_code,
            'post_code': self.post_code,
            'email': self.email,
            'is_active': self.is_active,
            'date_of_birth': self.date_of_birth.strftime('%d-%m-%Y'),
            'registration_date': self.registration_date.strftime('%d-%m-%Y')
        }