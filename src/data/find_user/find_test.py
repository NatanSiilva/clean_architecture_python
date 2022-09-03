from faker import Faker

from src.infra.test import UserRepositorySpy
from .find import FindUser

faker = Faker()


def test_by_id():
    """Testing by_id method"""

    user_repository = UserRepositorySpy()
    find_user = FindUser(user_repository)

    attribute = {"id": faker.random_number(digits=2)}
    response = find_user.by_id(user_id=attribute["id"])

    assert user_repository.select_user_params["user_id"] == attribute["id"]

    assert response["Success"] is True
    assert response["Data"] is not None


def test_by_name():
    """Testing by_name method"""

    user_repository = UserRepositorySpy()
    find_user = FindUser(user_repository)

    attribute = {"name": faker.name()}
    response = find_user.by_name(name=attribute["name"])

    assert user_repository.select_user_params["name"] == attribute["name"]
    assert response["Success"] is True
    assert response["Data"] is not None


def test_by_id_and_name():
    """Testing by_id_and_name method"""

    user_repository = UserRepositorySpy()
    find_user = FindUser(user_repository)

    attribute = {"id": faker.random_number(digits=2), "name": faker.name()}
    response = find_user.by_id_and_name(user_id=attribute["id"], name=attribute["name"])

    assert user_repository.select_user_params["user_id"] == attribute["id"]
    assert user_repository.select_user_params["name"] == attribute["name"]
    assert response["Success"] is True
    assert response["Data"] is not None


def test_by_id_invalid():
    """Testing by_id method with invalid id"""

    user_repository = UserRepositorySpy()
    find_user = FindUser(user_repository)

    attribute = {"id": faker.name()}
    response = find_user.by_id(user_id=attribute["id"])

    assert not user_repository.select_user_params
    assert response["Success"] is False
    assert response["Data"] is None


def test_by_name_invalid():
    """Testing by_name method with invalid name"""

    user_repository = UserRepositorySpy()
    find_user = FindUser(user_repository)

    attribute = {"name": faker.random_number(digits=2)}
    response = find_user.by_name(name=attribute["name"])

    assert not user_repository.select_user_params
    assert response["Success"] is False
    assert response["Data"] is None


def test_by_id_and_name_invalid():
    """Testing by_id_and_name method with invalid id and name"""

    user_repository = UserRepositorySpy()
    find_user = FindUser(user_repository)

    attribute = {"id": faker.name(), "name": faker.random_number(digits=2)}
    response = find_user.by_id_and_name(user_id=attribute["id"], name=attribute["name"])

    assert not user_repository.select_user_params
    assert response["Success"] is False
    assert response["Data"] is None
