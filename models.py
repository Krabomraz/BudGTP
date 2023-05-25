from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    profile_picture = db.Column(db.String(255))
    account_balance = db.Column(db.Numeric(precision=10, scale=2), default=0)
    # incomes = db.relationship('Income', backref='user', lazy=True)
    # debts = db.relationship('Debt', backref='user', lazy=True)
    expenses = db.relationship('Expense', backref='user', lazy=True)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    budget_limit = db.Column(db.Numeric(precision=10, scale=2), nullable=True)
    expenses = db.relationship('Expense', backref='category', lazy=True)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    amount = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    payment_method = db.Column(db.String(50))
    receipt_attachment = db.Column(db.String(255))

class Income(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    amount = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    source = db.Column(db.String(100))

# class Debt(db.Model):
#     __tablename__ = 'debts'

#     id = db.Column(db.Integer, primary_key=True)
#     description = db.Column(db.String(255), nullable=False)
#     amount = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
#     timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     creditor_name = db.Column(db.String(100))
#     creditor_contact = db.Column(db.String(100))

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    amount = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    transaction_type = db.Column(db.String(20))  # "expense" or "income"
    payment_method = db.Column(db.String(50))
    receipt_attachment = db.Column(db.String(255))
