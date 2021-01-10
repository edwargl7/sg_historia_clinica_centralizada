"""
PostgreSQL database.
Functions to manage the postgres database.

Useful information:
https://pynative.com/python-postgresql-tutorial/#:~:text=Use%20the%20connect()%20method,connection%20after%20your%20work%20completes.
"""

import psycopg2
from psycopg2 import Error

from database.database_interface import DatabaseInterface


class PostgresDatabase(DatabaseInterface):
    """PostgreSQL Database.

    Manage postgreSQL databases (connections and queries).
    """

    def __init__(self, db_credentials):
        super().__init__(db_credentials)

    def __connect_database(self):
        connection = None
        msg = ''
        try:
            connection = psycopg2.connect(**self._db_credentials)
            print('PostgreSQL connection created')
        except (Exception, Error) as error:
            msg = f'Error while connecting to PostgreSQL. {error}'
        finally:
            return connection, msg

    def __close_connection(self, connection, cursor=None):
        if connection:
            if cursor:
                cursor.close()
            connection.close()
            print('PostgreSQL connection is closed')

    def valid_connection(self) -> bool:
        connection, msg = self.__connect_database()
        if connection:
            connection.close()
            print('PostgreSQL connection is closed')
            return True
        else:
            print(msg)
            return False

    def query_all(self, query, args=None) -> list:
        connection, msg = self.__connect_database()
        cursor = None
        result = None
        try:
            if connection:
                cursor = connection.cursor()
                if args:
                    cursor.execute(query, args)
                else:
                    cursor.execute(query)
                result = cursor.fetchall()
        except (Exception, Error) as error:
            print(f'Error while querying the database. {error}')
        finally:
            self.__close_connection(connection, cursor)
            return result

    def query_many(self, n, query, args=None) -> list:
        connection, msg = self.__connect_database()
        cursor = None
        result = None
        try:
            if connection:
                cursor = connection.cursor()
                if args:
                    cursor.execute(query, args)
                else:
                    cursor.execute(query)
                result = cursor.fetchmany(n)
        except (Exception, Error) as error:
            print(f'Error while querying the database. {error}')
        finally:
            self.__close_connection(connection, cursor)
            return result

    def query_one(self, query, args=None) -> tuple:
        connection, msg = self.__connect_database()
        cursor = None
        result = None
        try:
            if connection:
                cursor = connection.cursor()
                if args:
                    cursor.execute(query, args)
                else:
                    cursor.execute(query)
                result = cursor.fetchone()
        except (Exception, Error) as error:
            print(f'Error while querying the database. {error}')
        finally:
            self.__close_connection(connection, cursor)
            return result
