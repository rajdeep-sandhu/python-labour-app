# repository.py
from abc import ABC, abstractmethod
from typing import Generator


class Repository[T](ABC):
    @abstractmethod
    def get(self, id: int) -> T:
        """Get item by id."""
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> Generator[T, None, None]:
        """Get all items."""
        raise NotImplementedError
