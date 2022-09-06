from src.presenters.controllers import FindUserController
from src.data.find_user import FindUser
from src.infra.repositories.user_repository import UserRepository


def find_user_composer() -> FindUserController:
    """
    Composing find user Route
    :param - None
    :return - Object with find user Route
    """

    user_repository = UserRepository()
    use_case = FindUser(user_repository)
    find_user_route = FindUserController(use_case)

    return find_user_route
