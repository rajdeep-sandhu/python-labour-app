from abc import ABC, abstractmethod

from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session


class DatabaseFactory(ABC):
    """Abstract factory for database resources."""

    @abstractmethod
    def create_engine(self) -> Engine:
        raise NotImplementedError

    @abstractmethod
    def create_session(self) -> Session:
        raise NotImplementedError
