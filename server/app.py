from flask import Flask, request, jsonify, Blueprint
from flask_restful import Api, Resource
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token
from models import Member, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookclub.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this in production

db.init_app(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

auth_bp = Blueprint('auth_bp', __name__, url_prefix='/authentication')
auth_api = Api(auth_bp)

class Login(Resource):
    def post(self):
        email = request.json.get("email", None)
        password = request.json.get("password", None)

        member = Member.query.filter_by(email=email).first()

        if member and bcrypt.check_password_hash(member.password, password):
            access_token = create_access_token(identity=member.id)
            return jsonify({"access_token": access_token})
        else:
            return jsonify({"message": "Invalid login credentials."}), 401

auth_api.add_resource(Login, '/login')
app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
