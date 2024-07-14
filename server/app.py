from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Book, MyShelf, Event  # Import Event model

# Book routes
@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = Book(
        picture=data['picture'],
        title=data['title'],
        category=data['category'],
        description=data['description'],
        price=data['price']
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify({"message": "Book successfully added"}), 201

@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    books_list = [
        {
            "id": book.id,
            "picture": book.picture,
            "title": book.title,
            "category": book.category,
            "description": book.description,
            "price": book.price
        }
        for book in books
    ]
    return jsonify(books_list), 200

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": "Book successfully deleted"}), 204

# MyShelf routes
@app.route('/MyShelf', methods=['POST'])
def add_to_my_shelf():
    data = request.get_json()
    new_shelf_book = MyShelf(
        picture=data['picture'],
        title=data['title'],
        category=data['category'],
        description=data['description'],
        price=data['price']
    )
    db.session.add(new_shelf_book)
    db.session.commit()
    return jsonify({"message": "Book successfully added to shelf"}), 201

@app.route('/MyShelf', methods=['GET'])
def get_my_shelf():
    my_shelf = MyShelf.query.all()
    my_shelf_list = [
        {
            "id": book.id,
            "picture": book.picture,
            "title": book.title,
            "category": book.category,
            "description": book.description,
            "price": book.price
        }
        for book in my_shelf
    ]
    return jsonify(my_shelf_list), 200

@app.route('/MyShelf/<int:id>', methods=['DELETE'])
def delete_from_my_shelf(id):
    shelf_book = MyShelf.query.get_or_404(id)
    db.session.delete(shelf_book)
    db.session.commit()
    return jsonify({"message": "Book successfully deleted from shelf"}), 204

# Event routes
@app.route('/events', methods=['POST'])
def add_event():
    data = request.get_json()
    
    # Extract book_id from data
    book_id = data.get('book_id')  # Assuming the frontend sends book_id along with event data
    
    # Check if the book exists
    book = Book.query.get(book_id)
    if not book:
        return jsonify({"message": f"Book with id {book_id} does not exist"}), 404
    
    new_event = Event(
        name=data['name'],
        location=data['location'],
        date=data['date'],
        book_id=book_id  # Assign the book_id to the event
    )
    db.session.add(new_event)
    db.session.commit()
    return jsonify({"message": "Event successfully added"}), 201

@app.route('/events', methods=['GET'])
def get_events():
    events = Event.query.all()
    events_list = [
        {
            "id": event.id,
            "name": event.name,
            "location": event.location,
            "date": event.date,
            "book_id": event.book_id  # Include book_id in the response
        }
        for event in events
    ]
    return jsonify(events_list), 200

@app.route('/events/<int:id>', methods=['DELETE'])
def delete_event(id):
    event = Event.query.get_or_404(id)
    db.session.delete(event)
    db.session.commit()
    return jsonify({"message": "Event successfully deleted"}), 204

if __name__ == '__main__':
    app.run(port=5000, debug=True)
