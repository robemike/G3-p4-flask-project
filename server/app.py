from flask import Flask 
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from models import db
from flask_cors import CORS
from datetime import timedelta
import random
from flask_jwt_extended import JWTManager
from events import events_bp, admin_bp
from auth import auth_bp
from books import books_bp
from members import members_bp 

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookclub.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = "fsbdgfnhgvjnvhmvh"+str(random.randint(1,1000000000000))
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=1)
app.config["SECRET_KEY"] = "JKSRVHJVFBSRDFV"+str(random.randint(1,1000000000000))
app.json.compact = False

app.register_blueprint(events_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(books_bp)
app.register_blueprint(members_bp)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

migrate = Migrate(app, db)
db.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app)

if __name__ == '__main__':
    app.run(port=5555, debug=True)