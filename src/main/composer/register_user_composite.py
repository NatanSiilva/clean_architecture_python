from src.main.interface import RouterInterface
from src.presenters.controllers import RegisterUserController
from src.data.register_user import RegisterUser
from src.infra.repositories.user_repository import UserRepository


def register_user_composer() -> RouterInterface:
    """
    Composing register user Route
    :param - None
    :return - Object with register user Route
    """

    repository = UserRepository()
    use_case = RegisterUser(repository)
    register_user_router = RegisterUserController(use_case)

    return register_user_router
