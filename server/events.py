from flask import Blueprint, request, jsonify, make_response
from flask_restful import Api, Resource
from models import Event, db

# Events blueprint
events_bp = Blueprint('events_bp', __name__, url_prefix='/events')
events_api = Api(events_bp)
class Events(Resource):
    
    def get(self):
        events = [event.to_dict() for event in Event.query.all()]
        return make_response(jsonify(events), 200)
    

# Admins blueprint.
admin_bp = Blueprint('admin_bp', __name__, url_prefix='/admin')
admin_api = Api(admin_bp)        
class AdminPost(Resource):
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
        
class AdminUpdateDelete(Resource):
    def patch(self, id):
        event = Event.query.filter(Event.id == id).first()
        for attr in request.form:
            setattr(event, attr, request.form[attr])
        db.session.add(event)
        db.session.commit()
        return make_response(event.to_dict(), 200)
        
    def delete(self, id):
        event = Event.query.filter_by(id = id).first()
        if event:
            db.session.delete(event)
            db.session.commit()
            return {"message": "Event deleted successfully."}, 200
        else:
            return {"message": "Event not found."}, 404

admin_api.add_resource(AdminPost, '/events')
admin_api.add_resource(AdminUpdateDelete, '/events/<int:id>')   
events_api.add_resource(Events, '/')