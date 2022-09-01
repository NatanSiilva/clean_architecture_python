from typing import List
from abc import ABC, abstractmethod

from src.domain.models import Users


class UserRepositoryInterface(ABC):
    """Interface to Pet Repository"""

    @abstractmethod
    def insert_user(self, name: str, password: str) -> Users:
        """abstractmethod"""
        raise Exception("Method not implemented")

    def select_user(self, user_id: int = None, name: str = None) -> List[Users]:
        """abstractmethod"""
        raise Exception("Method not implemented")
