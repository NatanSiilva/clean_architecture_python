from typing import List
from src.domain.models import Pets
from src.domain.test import mock_pet


class PetRepositorySpy:
    """Spy to Pet Repository"""

    def __init__(self):
        self.insert_pet_param = {}
        self.select_pet_param = {}

    def insert_pet(self, name: str, specie: str, age: int, user_id: int) -> Pets:
        """
        Spy all the attributes
        :param name: Pet name
        :param specie: Pet specie
        :param age: Pet age
        :param user_id: User id
        :return: Pet
        """

        self.insert_pet_param["name"] = name
        self.insert_pet_param["specie"] = specie
        self.insert_pet_param["age"] = age
        self.insert_pet_param["user_id"] = user_id

        return mock_pet()

    def select_pet(self, pet_id: int = None, user_id: int = None) -> List[Pets]:
        """Spy all the attributes"""

        self.select_pet_param["pet_id"] = pet_id
        self.select_pet_param["user_id"] = user_id

        return [mock_pet()]
