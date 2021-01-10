# from flask import Blueprint
#
# clinic_history_bp = Blueprint('')

from clinic_history.users.views import UserListResource


def initialize_routes(api):
    api.add_resource(UserListResource, '/users/',
                     endpoint='user_list_resource')
