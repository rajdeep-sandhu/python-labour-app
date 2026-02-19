from abc import ABC, abstractmethod

from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session


class DatabaseFactory(ABC):
    """Abstract factory for database resources."""

    @abstractmethod
    def create_engine(self) -> Engine:
        pass

    @abstractmethod
    def create_session(self) -> Session:
        pass
