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

if __name__ == '__main__':
    app.run(port=5000, debug=True)
