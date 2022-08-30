from collections import namedtuple
from src.infra.config import DBConnectionHandler

from src.infra.entities import Users


class UserRepository:
    """class to manage User Repository"""

    @staticmethod
    def insert_user(name: str, password: str) -> Users:
        """
        Insert a new user in the database
        :param - name: user name
        :param - password: user password
        :return : User object
        """

        InsertData = namedtuple("Users", "id name password")

        with DBConnectionHandler() as db_connection:
            try:
                new_user = Users(name=name, password=password)
                db_connection.session.add(new_user)
                db_connection.session.commit()

                return InsertData(
                    id=new_user.id, name=new_user.name, password=new_user.password
                )

            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
