from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from datetime import datetime
db = SQLAlchemy()

# members_events join table.
members_events = db.Table(
    'members_events',
    db.Column('member_id', db.Integer, db.ForeignKey(
        'members.id'), primary_key=True
        ),
    db.Column('event_id', db.Integer, db.ForeignKey(
        'events.id', primary_key=True)
        )
)

# Member model
class Member(db.Model):
    __tablename__ = "members"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

    # Relationship mapping Member(s) and Event(s)
    events = db.relationship(
        'Event', secondary=members_events, back_populates='members'
    )

# Event model
class Event(db.Model):
    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)

    # Relationship mapping Member(s) and Event(s)
    members = db.relationship(
        'Member', secondary=members_events, back_populates='events'
    )