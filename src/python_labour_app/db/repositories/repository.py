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

    @abstractmethod
    def get_by_criteria(self, criteria: dict[str, object]) -> Generator[T, None, None]:
        """Get items by criteria."""
        raise NotImplementedError

    @abstractmethod
    def add(self, **kwargs: object) -> None:
        """Add an item."""
        raise NotImplementedError

    @abstractmethod
    def update(self, id: int, **kwargs: object) -> None:
        """Update an item."""
        raise NotImplementedError
