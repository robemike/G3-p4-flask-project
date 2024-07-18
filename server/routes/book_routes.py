from flask import Blueprint, request, jsonify
from models import db, Book

book_bp = Blueprint('book_bp', __name__)

@book_bp.route('', methods=['POST'])
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

@book_bp.route('', methods=['GET'])
def get_books():
    books = Book.query.all()
    books_list = [book.as_dict() for book in books]
    return jsonify(books_list), 200

@book_bp.route('/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": "Book successfully deleted"}), 204

