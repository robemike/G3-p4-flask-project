from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from datetime import datetime
db = SQLAlchemy()

members_events = db.Table(
    'members_events',
    db.Column('member_id', db.Integer, db.ForeignKey(
        'members.id'), primary_key=True
        ),
    db.Column('event_id', db.Integer, db.ForeignKey(
        'events.id', primary_key=True)
        )
)

class Member(db.Model):
    __tablename__ = "members"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

    # Relationship mapping Member(s) and Event(s)
    events = db.relationship('Event', secondary=members_events, back_populates='members')
    
    reviews = db.relationship('Review', back_populates="member")

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

members_books = db.Table(
    'members_books',
    db.Column('member_id', db.Integer, db.ForeignKey(
        'members.id'), primary_key=True
        ),
    db.Column('book_id', db.Integer, db.ForeignKey(
        'books.id', primary_key=True)
        )
)

class Book(db.Model, SerializerMixin):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    author = db.Column(db.String)
    publisher_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    description = db.Column(db.text)

    b_events = db.relationship("review", secondary=members_books, back_populates='books')

class Review(db.Model, SerializerMixin):
    __tablename__ = "review"

    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column('member_id', db.Integer, db.ForeignKey('members.id', primary_key=True) )
    book_id= db.Column('book_id', db.Integer , db.ForeignKey('books.id', primary_key=True) )
    rating = db.Column(db.Integer)
    review = db.Column(db.String)

    member = db.relationship('Member', back_populates="reviews")