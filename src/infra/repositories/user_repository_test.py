from faker import Faker

from src.infra.config import DBConnectionHandler
from src.infra.entities import Users as UsersEntity
from .user_repository import UserRepository


faker = Faker()
user_repository = UserRepository()
db_connection_handler = DBConnectionHandler()


def test_insert_user():
    """
    Should insert a new user in the database
    """
    name = faker.name()
    password = faker.password()
    engine = db_connection_handler.get_engine()

    new_user = user_repository.insert_user(name, password)
    query = engine.execute(f"SELECT * FROM users WHERE id = {new_user.id}").fetchone()

    engine.execute(f"DELETE FROM users WHERE id = {new_user.id}")

    assert query is not None
    assert new_user.id == query.id
    assert new_user.name == query.name
    assert new_user.password == query.password


def test_select_user():
    """Shoul select a user in Users table and compare it"""

    user_id = faker.random_number(digits=5)
    name = faker.name()
    password = faker.word()
    data = UsersEntity(id=user_id, name=name, password=password)

    engine = db_connection_handler.get_engine()
    engine.execute(f"INSERT INTO users (id, name, password) VALUES ('{user_id}','{name}','{password}');")

    query_user_one = user_repository.select_user(user_id=user_id)
    query_user_two = user_repository.select_user(name=name)
    query_user_thee = user_repository.select_user(user_id=user_id, name=name)

    assert data in query_user_one
    assert data in query_user_two
    assert data in query_user_thee

    engine.execute(f"DELETE FROM users WHERE id='{user_id}';")
