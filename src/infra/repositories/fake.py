# pylint: disable=E1101

from src.infra.config import DBConnectionHandler
from src.infra.entities import Users


class FakerRepository:
    """A simple fake repository"""

    @staticmethod
    def insert_user(name: str, password: str) -> None:
        """Insert a user"""

        with DBConnectionHandler as db_connection:
            try:
                new_user = Users(name=name, password=password)
                db_connection.session.add(new_user)
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
            finally:
                db_connection.session.close()
