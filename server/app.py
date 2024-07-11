from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_migrate import Migrate
from flask_jwt_extended import jwt_required, create_access_token, create_refresh_token
from datetime import timedelta
from models import Member, Book, Review, Event, db
from flask_cors import CORS
from flask_bcrypt import Bcrypt
import random

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookclub.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = ""
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=1)
app.json.compact = False

bcrypt = Bcrypt(app)

migrate = Migrate(app, db)
db.init_app(app)
api = Api(app)

class SignUp(Resource):
    def post(self):
        data = request.form  
        existing_member = Member.query.filter_by(email=data['email']).first()
        if existing_member:
            return jsonify({"message": "Email address already exists, log in."}), 400
        hashed_password = bcrypt.generate_password_hash(data['password']).decode("utf-8")
        new_member = Member(username=data['username'], email=data['email'], password=hashed_password)
        db.session.add(new_member)
        db.session.commit()
        return jsonify({"message": "Signup successful."}), 201  # Or any appropriate success status

api.add_resource(SignUp, '/signup')

# class SignUp(Resource):
#     def post(self):
#         data = request.get_json()
#         existing_member = Member.query.filter_by(email=data['email']).first()
#         if existing_member:
#             return jsonify({"message": "Email address already exists, log in."}), 400
#         hashed_password = bcrypt.generate_password_hash(data['password']).decode("utf-8")
#         new_member = Member(username=data['username'], email=data['email'], password=hashed_password)
#         db.session.add(new_member)
#         db.session.commit()

# api.add_resource(SignUp, '/signup')

        

class Login(Resource):
    def post(self):
        email = request.json.get("email", None)
        password = request.json.get("password", None)

        member = Member.query.filter(Member.email == email).first()

        if member and bcrypt.check_password_hash(member.password, password):
            access_token = create_access_token(identity=member.id)
            return jsonify({"access_token":access_token})
        else:
            return jsonify({"message": "Invalid login credentials."})

api.add_resource(Login, '/login')




# Database setup
# engine = create_engine('sqlite:///bookclub.db')
# Base.metadata.bind = engine
# DBSession = sessionmaker(bind=engine)
# session = DBSession()

# # Member Resource
# class MemberResource(Resource):
#     def get(self, member_id=None):
#         if member_id:
#             member = session.query(Member).filter_by(id=member_id).first()
#             if member:
#                 return jsonify({
#                     'id': member.id,
#                     'username': member.username,
#                     'email': member.email,
#                     'books': [book.id for book in member.books],
#                     'events': [event.id for event in member.events]
#                 })
#             return {'message': 'Member not found'}, 404
#         members = session.query(Member).all()
#         return jsonify([{
#             'id': member.id,
#             'username': member.username,
#             'email': member.email
#         } for member in members])

#     def post(self):
#         data = request.json
#         new_member = Member(username=data['username'], email=data['email'], password=data['password'])
#         session.add(new_member)
#         session.commit()
#         return {'message': 'Member created', 'id': new_member.id}, 201

# # Book Resource
# class BookResource(Resource):
#     def get(self, book_id=None):
#         if book_id:
#             book = session.query(Book).filter_by(id=book_id).first()
#             if book:
#                 return jsonify({
#                     'id': book.id,
#                     'title': book.title,
#                     'author': book.author,
#                     'reviews': [review.id for review in book.reviews]
#                 })
#             return {'message': 'Book not found'}, 404
#         books = session.query(Book).all()
#         return jsonify([{
#             'id': book.id,
#             'title': book.title,
#             'author': book.author
#         } for book in books])

#     def post(self):
#         data = request.json
#         new_book = Book(title=data['title'], author=data['author'])
#         session.add(new_book)
#         session.commit()
#         return {'message': 'Book created', 'id': new_book.id}, 201

# # Review Resource
# class ReviewResource(Resource):
#     def get(self, review_id=None):
#         if review_id:
#             review = session.query(Review).filter_by(id=review_id).first()
#             if review:
#                 return jsonify({
#                     'id': review.id,
#                     'rating': review.rating,
#                     'comment': review.comment,
#                     'member_id': review.member_id,
#                     'book_id': review.book_id
#                 })
#             return {'message': 'Review not found'}, 404
#         reviews = session.query(Review).all()
#         return jsonify([{
#             'id': review.id,
#             'rating': review.rating,
#             'comment': review.comment,
#             'member_id': review.member_id,
#             'book_id': review.book_id
#         } for review in reviews])

#     def post(self):
#         data = request.json
#         new_review = Review(rating=data['rating'], comment=data['comment'], member_id=data['member_id'], book_id=data['book_id'])
#         session.add(new_review)
#         session.commit()
#         return {'message': 'Review created', 'id': new_review.id}, 201

# # Event Resource
# class EventResource(Resource):
#     def get(self, event_id=None):
#         if event_id:
#             event = session.query(Event).filter_by(id=event_id).first()
#             if event:
#                 return jsonify({
#                     'id': event.id,
#                     'name': event.name,
#                     'date': event.date,
#                     'members': [member.id for member in event.members]
#                 })
#             return {'message': 'Event not found'}, 404
#         events = session.query(Event).all()
#         return jsonify([{
#             'id': event.id,
#             'name': event.name,
#             'date': event.date
#         } for event in events])

#     def post(self):
#         data = request.json
#         new_event = Event(name=data['name'], date=data['date'])
#         session.add(new_event)
#         session.commit()
#         return {'message': 'Event created', 'id': new_event.id}, 201

# class Events(Resource):

#     def get(self):
#         events = Event.query.all()
#         events_list = [event.to_dict() for event in events]
#         return events_list
# # Endpoints
# api.add_resource(MemberResource, '/members', '/members/<int:member_id>')
# api.add_resource(BookResource, '/books', '/books/<int:book_id>')
# api.add_resource(ReviewResource, '/reviews', '/reviews/<int:review_id>')
# api.add_resource(EventResource, '/events', '/events/<int:event_id>')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
