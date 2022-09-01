from typing import List
from src.infra.config import DBConnectionHandler

from src.data.interfaces import UserRepositoryInterface
from src.domain.models import Users
from src.infra.entities import Users as UsersEntity


class UserRepository(UserRepositoryInterface):
    """class to manage User Repository"""

    @classmethod
    def insert_user(cls, name: str, password: str) -> Users:
        """
        Insert a new user in the database
        :param - name: user name
        :param - password: user password
        :return : User object
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_user = UsersEntity(name=name, password=password)
                db_connection.session.add(new_user)
                db_connection.session.commit()

                return Users(id=new_user.id, name=new_user.name, password=new_user.password)

            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

    @classmethod
    def select_user(cls, user_id: int = None, name: str = None) -> List[Users]:
        """
        Select data in user entity by id and/or name
        :param - user_id: Id of the registry
               - name: User name
        :return - List with Users selected
        """

        try:
            query_data = None

            if user_id and not name:

                with DBConnectionHandler() as db_connection:
                    data = db_connection.session.query(UsersEntity).filter_by(id=user_id).one()
                    query_data = [data]

            elif not user_id and name:

                with DBConnectionHandler() as db_connection:
                    data = db_connection.session.query(UsersEntity).filter_by(name=name).one()
                    query_data = [data]

            elif user_id and name:

                with DBConnectionHandler() as db_connection:
                    data = db_connection.session.query(UsersEntity).filter_by(id=user_id, name=name).one()
                    query_data = [data]

            return query_data
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()
