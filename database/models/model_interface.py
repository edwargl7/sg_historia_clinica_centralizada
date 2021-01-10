"""Model Interface

Interface to create functions fro querying the database tables,
similar to models.
"""
import abc


class ModelInterface(metaclass=abc.ABCMeta):
    """Model Interface.

    Interface to create functions fro querying the database tables,
    similar to models.
    """

    @staticmethod
    @abc.abstractmethod
    def get_all() -> list:
        """Get all the records of a table.

        :return: Returns all the records of a table
        """

    @staticmethod
    @abc.abstractmethod
    def get_by_id(pk_id) -> dict:
        """Get one record by ID.

        :param pk_id: primary key (id) of the record to search.
        :type pk_id: int

        :return:
        """

    @staticmethod
    @abc.abstractmethod
    def create(data) -> dict:
        """Create new record.

        :param data: Dict with field data to register.
        :type data: dict

        :return: Returns the created record.
        """

    @staticmethod
    @abc.abstractmethod
    def update(pk_id, data) -> dict:
        """Update record.

        :param pk_id: primary key (id) of the record to update.
        :type pk_id: int
        :param data: Dict with field data to update.
        :type data: dict

        :return: Returns the updated record.
        """
