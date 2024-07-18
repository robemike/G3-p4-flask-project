from flask import Blueprint, request, jsonify
from models import db, Event, Book

event_bp = Blueprint('event_bp', __name__)

@event_bp.route('', methods=['POST'])
def add_event():
    data = request.get_json()
    book_id = data.get('book_id')
    book = Book.query.get(book_id)
    if not book:
        return jsonify({"message": f"Book with id {book_id} does not exist"}), 404

    new_event = Event(
        name=data['name'],
        location=data['location'],
        date=data['date'],
        book_id=book_id
    )
    db.session.add(new_event)
    db.session.commit()
    return jsonify({"message": "Event successfully added"}), 201

@event_bp.route('', methods=['GET'])
def get_events():
    events = Event.query.all()
    events_list = [event.as_dict() for event in events]
    return jsonify(events_list), 200

@event_bp.route('/<int:id>', methods=['DELETE'])
def delete_event(id):
    event = Event.query.get_or_404(id)
    db.session.delete(event)
    db.session.commit()
    return jsonify({"message": "Event successfully deleted"}), 204
