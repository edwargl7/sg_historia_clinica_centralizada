"""User views"""
import json

from flask import request, Response
from flask_restful import Resource

# Models
from clinic_history.users.models import User
# Utils
from database.models.error_handling import object_not_found_by_id
from database.utils.json_util import json_serial


class UserListResource(Resource):
    @staticmethod
    def get():
        users = User.get_all()
        users = json.dumps(users, default=json_serial,
                           ensure_ascii=False)
        if users:
            users = users.encode('utf8')
        return Response(users,
                        mimetype="application/json",
                        status=200)

    @staticmethod
    def post():
        data = request.get_json()
        user = User.create(data)
        if user:
            user = user.encode('utf8')
        return Response(user,
                        mimetype="application/json",
                        status=200)


class UserResource(Resource):

    @staticmethod
    def get(user_id):
        user = User.get_by_id(user_id)
        if user is None:
            return object_not_found_by_id('User', user_id)

        user = json.dumps(user, default=json_serial,
                          ensure_ascii=False)
        if user:
            user = user.encode('utf8')
        return Response(user,
                        mimetype="application/json",
                        status=200)

    @staticmethod
    def put(user_id):
        user = User.get_by_id(user_id)
        if user is None:
            return object_not_found_by_id('User', user_id)

        data = request.get_json()
        user = User.update(user_id, data)
        if user:
            user = user.encode('utf8')
        return Response(user,
                        mimetype="application/json",
                        status=200)
