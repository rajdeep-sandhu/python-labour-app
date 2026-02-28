# repository.py
from abc import ABC, abstractmethod

class Repository[T](ABC):
    @abstractmethod
    def get(self, id: int) -> T:
        """Get item by id."""
        raise NotImplementedError
    