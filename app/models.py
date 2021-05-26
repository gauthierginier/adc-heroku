from enum import unique
from flask_login import UserMixin
from . import db

class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    firstname = db.Column(db.String(100))
    surname = db.Column(db.String(100))
    
class Skills(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, unique=False)
    person_id = db.Column(db.Integer, db.ForeignKey('users.id'),
        nullable=False)
    ref = db.Column(db.String(100))
    points = db.Column(db.Integer)

