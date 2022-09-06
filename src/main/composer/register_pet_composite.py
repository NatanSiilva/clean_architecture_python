from src.infra.repositories.pet_repository import PetRepository
from src.infra.repositories.user_repository import UserRepository
from src.data.registry_pet import RegisterPet
from src.data.find_user import FindUser
from src.presenters.controllers import RegisterPetController


def register_pet_composer() -> RegisterPetController:
    """
    Composing register Pet Route
    :param - None
    :return - Object with register Pet Route
    """

    repository = PetRepository()
    find_user_use_case = FindUser(UserRepository())
    use_case = RegisterPet(repository, find_user_use_case)
    register_pet_router = RegisterPetController(use_case)

    return register_pet_router
