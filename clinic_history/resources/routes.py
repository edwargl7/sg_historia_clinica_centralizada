"""Routes"""
from clinic_history.users.views import UserListResource
from clinic_history.users.views import UserResource
from clinic_history.user_types.views import UserTypeListResource
from clinic_history.user_types.views import UserTypeResource


def initialize_routes(api):
    api.add_resource(UserListResource, '/users/',
                     endpoint='user_list_resource')
    api.add_resource(UserResource, '/users/<int:user_id>',
                     endpoint='user_resource')

    api.add_resource(UserTypeListResource, '/user_types/',
                     endpoint='user_type_list_resource')
    api.add_resource(UserTypeResource, '/user_types/<int:user_type_id>',
                     endpoint='user_type_resource')

