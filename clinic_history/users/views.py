"""User views"""
import json
from database.utils.json_util import json_serial
from flask import request, Response
from flask_restful import Resource

# Models
from clinic_history.users.models import User


class UserListResource(Resource):
    @staticmethod
    def get():
        users = User.get_all()
        users = json.dumps(users, default=json_serial, ensure_ascii=False)
        if users:
            users = users.encode('utf8')
        return Response(users,
                        mimetype="application/json",
                        status=200
                        )

    @staticmethod
    def post():
        pass


class UserResource(Resource):

    @staticmethod
    def get(user_id):
        user = User.get_by_id(user_id)
        user = json.dumps(user, default=json_serial, ensure_ascii=False)
        if user:
            user = user.encode('utf8')
        return Response(user,
                        mimetype="application/json",
                        status=200
                        )

    @staticmethod
    def put(user_id):
        pass
