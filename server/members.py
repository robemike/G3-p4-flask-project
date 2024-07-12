
from flask import Blueprint, request, jsonify, make_response
from flask_restful import Api, Resource
from models import Member, db

members_bp = Blueprint('members_bp', __name__, url_prefix='/members')
members_api = Api(members_bp)

class Members(Resource):
    def get(self):
        members = [member.to_dict() for member in Member.query.all()]
        return make_response(jsonify(members), 200)


class MemberById(Resource):
    def get(self, id):
        member = Member.query.filter_by(id=id).first()
        if not member:
            return {"message": "Member not found."}, 404
        return make_response(jsonify(member.to_dict()), 200)

    def patch(self, id):
        member = Member.query.filter_by(id=id).first()
        if not member:
            return {"message": "Member not found."}, 404

        for attr in request.form:
            setattr(member, attr, request.form[attr])

        db.session.add(member)
        db.session.commit()
        return make_response(jsonify(member.to_dict()), 200)

    def delete(self, id):
        member = Member.query.filter_by(id=id).first()
        if not member:
            return {"message": "Member not found."}, 404

        db.session.delete(member)
        db.session.commit()
        return {"message": "Member deleted successfully."}, 200

members_api.add_resource(Members, '/')
members_api.add_resource(MemberById, '/<int:id>')
