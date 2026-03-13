# repository.py
from abc import ABC, abstractmethod
from typing import Generator


class Repository[T](ABC):
    @abstractmethod
    def get(self, id: int) -> T | None:
        """Get item by id."""
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> list[T]:
        """Get all items."""
        raise NotImplementedError

    @abstractmethod
    def get_by_criteria(self, criteria: dict[str, object]) -> list[T]:
        """Get items by criteria."""
        raise NotImplementedError

    @abstractmethod
    def add(self, **kwargs: dict[str, object]) -> T | None:
        """Add an item."""
        raise NotImplementedError

    @abstractmethod
    def update(self, id: int, **kwargs: dict[str, object]) -> T | None:
        """Update an item."""
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: int) -> None:
        """Delete an item."""
        raise NotImplementedError
