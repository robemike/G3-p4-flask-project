from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

# members_events join table.
members_events = db.Table(
    'members_events',
    db.Column('member_id', db.Integer, db.ForeignKey('members.id')),  # Remove 'primary_key=True'
    db.Column('event_id', db.Integer, db.ForeignKey('events.id')),  # Remove 'primary_key=True'
)
# Member gmodel
class Member(db.Model):
    __tablename__ = "members"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

    # Relationship mapping Member(s) and Event(s).
    events = db.relationship(
        'Event', secondary=members_events, back_populates='members'
    )
    reviews = db.relationship('Review', back_populates='member', cascade='all, delete-orphan')
    books = association_proxy('reviews', 'book',
                              creator= lambda book_obj: Review(book=book_obj))

    def generate_password_hash(self, password):
        self.password = generate_password_hash(password).decode('utf-8')

    
    

# Event model
class Event(db.Model):
    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)

    # Relationship mapping Member(s) and Event(s)
    members = db.relationship(
        'Member', secondary=members_events, back_populates='events'
    )

class Book(db.Model, SerializerMixin):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    author = db.Column(db.String)
    published_date = db.Column(db.DateTime)

    reviews = db.relationship('Review', back_populates='book', cascade='all, delete-orphan')
    members = association_proxy('reviews', 'member',
                                creator= lambda member_obj: Review(member=member_obj))

class Review(db.Model, SerializerMixin):
    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.String)
    rating = db.Column(db.Integer)

    member_id = db.Column(db.Integer, db.ForeignKey('members.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))

    member = db.relationship('Member', back_populates='reviews')
    book = db.relationship('Book', back_populates='reviews')