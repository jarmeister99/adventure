from datetime import datetime

from app import db


class Trip(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(200), index=True, unique=True)
    activity = db.Column(db.String(100))
    location = db.Column(db.String(100))
    cost = db.Column(db.Float)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    # one to many - one trip, many users signed up
    signed_up = db.relationship('User', backref='signed_up_for', lazy='dynamic')


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    position = db.Column(db.Integer, index=True, unique=True)
    name = db.Column(db.String(200))
    email = db.Column(db.String(200), index=True, unique=True)
    phone_number = db.Column(db.String(8), index=True, unique=True)
    paid = db.Column(db.Boolean)
    is_driver = db.Column(db.Boolean)
    pin = db.Column(db.SmallInteger, unique=True)
    trip_id = db.Column(db.Integer, db.ForeignKey('trip.id'))
