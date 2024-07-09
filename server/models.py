from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

members_books = Table('members_books', Base.metadata,
    Column('member_id', Integer, ForeignKey('members.id')),
    Column('book_id', Integer, ForeignKey('books.id'))
)

members_events = Table('members_events', Base.metadata,
    Column('member_id', Integer, ForeignKey('members.id')),
    Column('event_id', Integer, ForeignKey('events.id'))
)

class Member(Base):
    __tablename__ = 'members'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    reviews = relationship('Review', back_populates='member')
    books = relationship('Book', secondary='members_books', back_populates='members')
    events = relationship('Event', secondary='members_events', back_populates='members')

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    reviews = relationship('Review', back_populates='book')
    members = relationship('Member', secondary='members_books', back_populates='books')

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    rating = Column(Integer, nullable=False)
    comment = Column(String)
    member_id = Column(Integer, ForeignKey('members.id'))
    book_id = Column(Integer, ForeignKey('books.id'))
    member = relationship('Member', back_populates='reviews')
    book = relationship('Book', back_populates='reviews')

class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    date = Column(String, nullable=False)
    members = relationship('Member', secondary='members_events', back_populates='events')
