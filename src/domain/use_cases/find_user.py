from typing import List, Dict
from abc import ABC, abstractmethod

from src.domain.models import Users


class FindUser(ABC):
    """
    Abstract interface to FindUser use case
    """

    @abstractmethod
    def by_id(self, user_id: int) -> Dict[bool, List[Users]]:
        """Specific implementation use case"""

        raise Exception("Should implement method: by_id")

    @abstractmethod
    def by_name(self, name: str) -> Dict[bool, List[Users]]:
        """Specific implementation use case"""

        raise Exception("Should implement method: by_name")

    @abstractmethod
    def by_id_and_name(self, user_id: int, name: str) -> Dict[bool, List[Users]]:
        """Specific implementation use case"""

        raise Exception("Should implement method: user_id, name")
