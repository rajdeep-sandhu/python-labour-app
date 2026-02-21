import os

from sqlalchemy import URL, create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker

from .database_factory import DatabaseFactory


class SQLiteFactory(DatabaseFactory):
    """Concrete sqlite factory."""

    def __init__(self, url: str = "sqlite+pysqlite:///:memory:") -> None:
        self._engine = create_engine(url)

        self._sessionmaker = sessionmaker(
            bind=self._engine, autoflush=False, autocommit=False
        )
