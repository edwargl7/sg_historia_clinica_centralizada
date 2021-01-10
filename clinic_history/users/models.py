""" User models"""
# Interface
from database.models.model_interface import ModelInterface

# Database
from settings.settings import DB


class User(ModelInterface):
    """User Model"""

    @staticmethod
    def get_all() -> list:
        result = DB.query_all("get_users")
        return result

    @staticmethod
    def get_by_id(pk_id) -> dict:
        result = DB.query_one("get_user", (pk_id,))
        return result

    @staticmethod
    def create(data) -> dict:
        pass

    @staticmethod
    def update(pk_id, data) -> dict:
        pass
