from faker import Faker

from src.data.test import FindUserSpy
from src.presenters.helpers import HttpRequest
from src.infra.test import UserRepositorySpy
from .find_user_controller import FindUserController

faker = Faker()


def test_handle():
    """Testing Handle method"""

    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)
    http_request = HttpRequest(query={"user_id": faker.random_number(digits=3), "user_name": faker.word()})

    response = find_user_controller.handle(http_request)

    assert find_user_use_case.by_id_and_name_param["user_id"] == http_request.query["user_id"]
    assert find_user_use_case.by_id_and_name_param["name"] == http_request.query["user_name"]

    assert response.status_code == 200
    assert response.body is not None


def test_handle_with_no_query():
    """Testing Handle method with no query"""

    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)
    http_request = HttpRequest()

    response = find_user_controller.handle(http_request)

    assert not find_user_use_case.by_id_and_name_param
    assert not find_user_use_case.by_id_param
    assert not find_user_use_case.by_name_param

    assert response.status_code == 400
    assert "error" in response.body
