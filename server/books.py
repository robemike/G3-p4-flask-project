from flask import Blueprint, make_response, jsonify, request
from flask_restful import Resource, Api
from models import Book, db

books_bp = Blueprint('books_bp', __name__, url_prefix='/books')
books_api = Api(books_bp)

class Books(Resource):
    def get(self):
        books = [book.to_dict() for book in Book.query.all()]
        return make_response(jsonify(books), 200)
    
    def post(self):
        title = request.form.get('title')
        author = request.form.get('author')
        publication_year = request.form.get('publication_year')

        existing_book = Book.query.filter_by(title=title).first()
        if existing_book:
            return {"message": "Book already exists."}, 400
        else:
            new_book = Book(title=title, author=author, publication_year=publication_year)
            db.session.add(new_book)
            db.session.commit()
            return {"message": "Book created successfully."}, 201
    
class BookById(Resource):
    def patch(self, id):
        book = Book.query.filter_by(id=id).first()
        if not book:
            return {"message": "Book not found."}, 404

        for attr in request.form:
            setattr(book, attr, request.form[attr])

        db.session.add(book)
        db.session.commit()
        return make_response(book.to_dict(), 200)
    
    def delete(self, id):
        book = Book.query.filter_by(id=id).first()
        if not book:
            return {"message": "Book not found."}, 404

        db.session.delete(book)
        db.session.commit()
        return {"message": "Book deleted successfully."}, 200
    
books_api.add_resource(BookById, '/<int:id>')
books_api.add_resource(Books, '/')