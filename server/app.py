from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api
from flask_migrate import Migrate
from flask_jwt_extended import jwt_required, create_access_token, create_refresh_token, JWTManager
from datetime import timedelta
from models import Member, Book, Review, Event, db
from flask_cors import CORS
from flask_bcrypt import Bcrypt
import random

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookclub.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = "fsbdgfnhgvjnvhmvh"+str(random.randint(1,1000000000000))
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=1)
app.config["SECRET_KEY"] = "JKSRVHJVFBSRDFV"+str(random.randint(1,1000000000000))
app.json.compact = False

bcrypt = Bcrypt(app)
jwt = JWTManager(app)

migrate = Migrate(app, db)
db.init_app(app)
api = Api(app)


class SignUp(Resource):
    def post(self):
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        existing_member = Member.query.filter_by(email=email).first()
        if existing_member:
            return {"message": "Email address already exists."}, 400
        else:
            hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
            new_member = Member(username=username, email=email, password=hashed_password)
            db.session.add(new_member)
            db.session.commit()
            return {"message": "Member registered successfully."}
        
class Login(Resource):
    def post(self):
        email = request.form.get("email", None)
        password = request.form.get("password", None)

        member = Member.query.filter(Member.email == email).first()

        if member and bcrypt.check_password_hash(member.password, password):
            access_token = create_access_token(identity=member.id)
            return jsonify({"access_token":access_token})
        else:
            return jsonify({"message": "Invalid login credentials."})

class Events(Resource):
    
    def post(self):
        name = request.form.get('name')
        date = request.form.get('date')
        location = request.form.get('location')
        description = request.form.get('description')

        existing_event = Event.query.filter(Event.name == name).first()
        if existing_event:
            return {"message": "Event already exists."}, 400
        else:
            new_event = Event(name=name, date=date, location=location, description=description)
            db.session.add(new_event)
            db.session.commit()
            return {"message": "Event created successfully."}, 201
        
    def get(self):
        events = [event.to_dict() for event in Event.query.all()]
        return make_response(jsonify(events), 200)        

api.add_resource(SignUp, '/signup')
api.add_resource(Login, '/login')
api.add_resource(Events, '/event')

if __name__ == '__main__':
    app.run(port=5555, debug=True)