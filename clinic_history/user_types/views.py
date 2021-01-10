"""User Types views"""
import json

from flask import request, Response
from flask_restful import Resource

# Models
from clinic_history.user_types.models import UserType
# Utils
from database.models.error_handling import object_not_found_by_id
from database.utils.json_util import json_serial


class UserTypeListResource(Resource):
    @staticmethod
    def get():
        user_types = UserType.get_all()

        if user_types:
            user_types = json.dumps(user_types,
                                    default=json_serial,
                                    ensure_ascii=False)
            user_types = user_types.encode('utf8')
        return Response(user_types,
                        mimetype="application/json",
                        status=200)

    @staticmethod
    def post():
        data = request.get_json()
        user_type = UserType.create(data)
        if user_type:
            user_type = json.dumps(user_type,
                                   default=json_serial,
                                   ensure_ascii=False)
            user_type = user_type.encode('utf8')
        return Response(user_type,
                        mimetype="application/json",
                        status=200)


class UserTypeResource(Resource):

    @staticmethod
    def get(user_type_id):
        user_type = UserType.get_by_id(user_type_id)
        if user_type is None:
            return object_not_found_by_id('User', user_type_id)

        user_type = json.dumps(user_type, default=json_serial,
                               ensure_ascii=False)
        if user_type:
            user_type = user_type.encode('utf8')
        return Response(user_type,
                        mimetype="application/json",
                        status=200)

    @staticmethod
    def put(user_type_id):
        user_type = UserType.get_by_id(user_type_id)
        if user_type is None:
            return object_not_found_by_id('User Type', user_type_id)

        data = request.get_json()
        user_type = UserType.update(user_type_id, data)
        if user_type:
            user_type = user_type.encode('utf8')
        return Response(user_type,
                        mimetype="application/json",
                        status=200)
