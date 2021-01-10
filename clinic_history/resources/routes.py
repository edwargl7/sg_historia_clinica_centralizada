"""Routes"""
from clinic_history.users.views import UserListResource
from clinic_history.users.views import UserResource


def initialize_routes(api):
    api.add_resource(UserListResource, '/users/',
                     endpoint='user_list_resource')
    api.add_resource(UserResource, '/users/<int:user_id>',
                     endpoint='user_resource')
