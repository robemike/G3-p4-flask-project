from flask import Blueprint, request, jsonify
from models import db, MyShelf

myshelf_bp = Blueprint('myshelf_bp', __name__)

@myshelf_bp.route('', methods=['POST'])
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

@myshelf_bp.route('', methods=['GET'])
def get_my_shelf():
    my_shelf = MyShelf.query.all()
    my_shelf_list = [book.as_dict() for book in my_shelf]
    return jsonify(my_shelf_list), 200

@myshelf_bp.route('/<int:id>', methods=['DELETE'])
def delete_from_my_shelf(id):
    shelf_book = MyShelf.query.get_or_404(id)
    db.session.delete(shelf_book)
    db.session.commit()
    return jsonify({"message": "Book successfully deleted from shelf"}), 204
