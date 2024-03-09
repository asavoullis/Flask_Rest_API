from models.extensions import db

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_number = db.Column(db.String(20), unique=True, nullable=False)
    balance = db.Column(db.Float, default=0.0, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    account_type = db.Column(db.String(20), nullable=False)

    currency = db.Column(db.String(3), default='USD')
    
    # 1 = Active (True)
    is_active = db.Column(db.Boolean, default=True)

    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())  
    last_updated_at = db.Column(db.DateTime, onupdate=db.func.current_timestamp())  

    credit = db.Column(db.Float, default=0.0)
    debit = db.Column(db.Float, default=0.0)   

    def __repr__(self):
        return f'<Account {self.account_number}>'

    def to_dict(self):
        return {
            'id': self.id,
            'account_number': self.account_number,
            'balance': self.balance,
            'user_id': self.user_id,
            'account_type': self.account_type,
            'currency': self.currency,
            'is_active': self.is_active,
            'created_at': self.created_at,
            'last_updated_at': self.last_updated_at,
            'credit': self.credit,
            'debit': self.debit
        }