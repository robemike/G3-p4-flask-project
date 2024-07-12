from flask import Flask, request, jsonify, Blueprint
from flask_restful import Resource, Api
from flask_jwt_extended import create_access_token, JWTManager, jwt_required, get_jwt_header
from models import Member, db
from flask_bcrypt import Bcrypt

auth_bp = Blueprint('auth_bp', __name__, url_prefix='/authentication')
bcrypt = Bcrypt()
jwt = JWTManager()
auth_api = Api(auth_bp)

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
        username = request.form.get('username', None)
        email = request.form.get("email", None)
        password = request.form.get("password", None)

        member_username = Member.query.filter_by(username = username).first()
        member_email = Member.query.filter(Member.email == email).first()

        if member_email and member_username and bcrypt.check_password_hash(member_email.password, password):
            access_token = create_access_token(identity=member_email.id)
            return jsonify({"access_token":access_token})
        else:
            return jsonify({"message": "Invalid login credentials."})

auth_api.add_resource(SignUp, '/signup')
auth_api.add_resource(Login, '/login')