"""Database Factory"""
from database.database_interface import DatabaseInterface
from database.postgres_database import PostgresDatabase


class DatabaseFactory:

    @staticmethod
    def get_manage_database(database, db_credentials) -> DatabaseInterface:
        """Get Manage Database by database name.

        :param database: database name.
        :type database: str
        :param db_credentials: database credentials.
        :type db_credentials: dict

        :raises ValueError: Database name not found

        :return: manage database.
        """
        if database == 'postgres':
            return PostgresDatabase(db_credentials)
        else:
            raise ValueError(database)
