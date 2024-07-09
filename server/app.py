#!/usr/bin/env python

from flask import Flask 
from flask_migrate import Migrate

from models import db, Member

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app=app, db=db)
db.init_app(app)

if __name__ == "__main":
    app.run(port=5555, debug=True)