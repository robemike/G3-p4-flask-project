from flask import Flask, render_template, request, jsonify
from flask_login import LoginManager, login_user, current_user, logout_user
from models import Member
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_secret_key'  # Replace with a strong secret key

bcrypt = Bcrypt(app)
jwt = JWTManager(app)

migrate = Migrate(app=app, db=db)
db.init_app(app)

# ... other routes and logic (replace with your application logic)

@app.route('/login', methods=['POST'])
def login():
    if current_user.is_authenticated:
        return jsonify({'error': 'Already logged in'})

    username = request.json.get('username')
    password = request.json.get('password')

    user = Member.query.filter_by(email=username).first()
    if user and bcrypt.check_password_hash(user.password, password):
        # Generate JWT access token
        access_token = create_access_token(identity=user.id)
        return jsonify({'success': True, 'access_token': access_token})
    else:
        return jsonify({'error': 'Invalid credentials'})

if __name__ == "__main__":
    app.run(port=5555, debug=True)
