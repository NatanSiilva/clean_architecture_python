from typing import List, Dict, Type

from src.data.interfaces import UserRepositoryInterface as UserRepository
from src.domain.use_cases import FindUser as FindUserInterface
from src.domain.models import Users


class FindUser(FindUserInterface):
    """
    FindUser use case implementation
    """

    def __init__(self, user_repository: Type[UserRepository]):
        self.user_repository = user_repository

    def by_id(self, user_id: int) -> Dict[bool, List[Users]]:
        """
        Specific implementation use case
        :param - user_id: id of user
        :return - dictionary: Dictionary with information about the process
        """

        response = None
        validate_entry = isinstance(user_id, int)

        if validate_entry:
            response = self.user_repository.select_user(user_id=user_id)

        return {"Success": validate_entry, "Data": response}

    def by_name(self, name: str) -> Dict[bool, List[Users]]:
        """
        Specific implementation use case
        :param - name: name of user
        :return - dictionary: Dictionary with information about the process
        """

        response = None
        validate_entry = isinstance(name, str)

        if validate_entry:
            response = self.user_repository.select_user(name=name)

        return {"Success": validate_entry, "Data": response}

    def by_id_and_name(self, user_id: int, name: str) -> Dict[bool, List[Users]]:
        """
        Specific implementation use case
        :param - user_id: id of user
        :param - name: name of user
        :return - dictionary: Dictionary with information about the process
        """

        response = None
        validate_entry = isinstance(user_id, int) and isinstance(name, str)

        if validate_entry:
            response = self.user_repository.select_user(user_id=user_id, name=name)

        return {"Success": validate_entry, "Data": response}
