# repository.py
from abc import ABC, abstractmethod


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
    def add(self, entity: T) -> T:
        """Add an item."""
        raise NotImplementedError

    @abstractmethod
    def update(self, entity: T) -> T | None:
        """
        Update an item.
        This method is essentially a NOP.
        The actual update occurs in the identity map and is persisted via a flush.
        """
        raise NotImplementedError

    @abstractmethod
    def delete(self, entity: T) -> None:
        """Delete an item."""
        raise NotImplementedError
