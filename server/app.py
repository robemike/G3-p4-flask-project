import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy and Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import models (assuming they are defined in models.py)
from models import Book, MyShelf, Event

# Register blueprints
from routes.book_routes import book_bp
from routes.myshelf_routes import myshelf_bp
from routes.event_routes import event_bp

app.register_blueprint(book_bp, url_prefix='/api/books')
app.register_blueprint(myshelf_bp, url_prefix='/api/myshelf')
app.register_blueprint(event_bp, url_prefix='/api/events')

if __name__ == '__main__':
    app.run(port=5000, debug=True)

