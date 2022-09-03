from faker import Faker

from src.infra.test import UserRepositorySpy
from .register import RegisterUser

faker = Faker()


def test_register():
    """Testing register user"""

    user_repository = UserRepositorySpy()
    register_user = RegisterUser(user_repository=user_repository)

    attributes = {
        "name": faker.name(),
        "password": faker.password(),
    }

    response = register_user.register(**attributes)

    assert user_repository.insert_user_params["name"] == attributes["name"]
    assert user_repository.insert_user_params["password"] == attributes["password"]

    assert response["Success"] is True
    assert response["Data"] is not None


def test_register_fail():
    """Testing register user in fail"""

    user_repository = UserRepositorySpy()
    register_user = RegisterUser(user_repository=user_repository)

    attributes = {
        "name": faker.random_number(digits=5),
        "password": faker.random_number(digits=5),
    }

    response = register_user.register(**attributes)

    assert not user_repository.insert_user_params

    assert response["Success"] is False
    assert response["Data"] is None
