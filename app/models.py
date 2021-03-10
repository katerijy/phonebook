from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    phone = db. Column(db.Integer(), nullable=False, unique=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)

    def __init__(self, username, phone, email, password):
        self.username = username
        self.email = email
        self.phone = phone
        self.password = generate_password_hash(password)

    def __repr__(self):
        return f'<User: {self.username} | {self.password}, {self.email}, {self.phone}>'

