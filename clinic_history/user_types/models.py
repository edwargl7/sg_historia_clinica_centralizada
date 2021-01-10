""" User Type models"""
# Interface
from database.models.model_interface import ModelInterface

# Database
from settings.settings import DB


class UserType(ModelInterface):
    """User Type Model"""

    @staticmethod
    def get_all() -> list:
        result = DB.query_all("select * from get_user_types();")
        return result

    @staticmethod
    def get_by_id(pk_id) -> dict:
        result = DB.query_one("select * from get_user_type(%s);", (pk_id,))
        return result

    @staticmethod
    def create(data) -> dict:
        result = DB.query_one("select * from get_user_type(%s);", (data,))
        return result

    @staticmethod
    def update(pk_id, data) -> dict:
        result = DB.query_one("select * from get_user_type(%s);", (pk_id,))
        return result
