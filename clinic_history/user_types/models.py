""" User Type models"""
# Interface
from database.models.model_interface import ModelInterface

# Database
from settings.settings import DB


class UserType(ModelInterface):
    """User Type Model"""

    @staticmethod
    def get_all() -> list:
        result = DB.query_all("get_user_types")
        print("Este es el resultado")
        print(result)
        return result

    @staticmethod
    def get_by_id(pk_id) -> dict:
        result = DB.query_one("get_user_type", (pk_id,))
        return result

    @staticmethod
    def create(data) -> dict:
        name = data['name']
        result = DB.query_one("create_user_type", (name,), True)
        return result

    @staticmethod
    def update(pk_id, data) -> dict:
        result = DB.query_one("update_user_type", (pk_id, data,), True)
        return result
