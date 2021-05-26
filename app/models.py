from enum import unique
from flask_login import UserMixin
from . import db

class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    tel = db.Column(db.String(15), unique=True)
    password = db.Column(db.String(100))
    username = db.Column(db.String(100), unique=True)
    firstname = db.Column(db.String(100))
    surname = db.Column(db.String(100))
    
class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, unique=False)
    person_id = db.Column(db.Integer, db.ForeignKey('users.id'),
        nullable=False)
    lat = db.Column(db.String(100))
    lng = db.Column(db.String(100))
    city = db.Column(db.String(100))
    zip = db.Column(db.Integer)
    country = db.Column(db.String(100))
    qrcode_data = db.Column(db.String(100))
