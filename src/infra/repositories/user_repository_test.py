from faker import Faker

from src.infra.config import DBConnectionHandler
from .user_repository import UserRepository

faker = Faker()
user_repository = UserRepository()
db_connection = DBConnectionHandler()


def test_insert_user():
    """
    Should insert a new user in the database
    """
    name = faker.name()
    password = faker.password()
    engine = db_connection.get_engine()

    new_user = user_repository.insert_user(name, password)
    query = engine.execute(f"SELECT * FROM users WHERE id = {new_user.id}").fetchone()

    engine.execute(f"DELETE FROM users WHERE id = {new_user.id}")

    assert query is not None
    assert new_user.id == query.id
    assert new_user.name == query.name
    assert new_user.password == query.password
