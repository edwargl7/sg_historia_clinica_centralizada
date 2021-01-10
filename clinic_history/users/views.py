"""User views"""
import json
from database.utils.json_util import json_serial
from flask import request, jsonify, Response
from flask_restful import Resource

# Models
from clinic_history.users.models import User


class UserListResource(Resource):
    @staticmethod
    def get():
        users = User.get_all()
        users = json.dumps(users, default=json_serial, ensure_ascii=False)
        return Response(users.encode('utf8'),
                        mimetype="application/json",
                        status=200
                        )

    @staticmethod
    def post():
        pass


class UserResource(Resource):

    @staticmethod
    def get(user_id):
        users = User.get_all()
        return jsonify(users)

    @staticmethod
    def put(user_id):
        pass
