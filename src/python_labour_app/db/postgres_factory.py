import os

from sqlalchemy import URL, create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker

from .database_factory import DatabaseFactory


class PostgresFactory(DatabaseFactory):
    """Concrete postgres factory."""

    def __init__(self) -> None:
        self._username = os.environ["POSTGRES_USER"]
        self._password = os.environ["POSTGRES_PASSWORD"]
        self._database = os.environ["POSTGRES_DB"]
        self._host = os.environ.get("POSTGRES_HOST", "localhost")
        self._port = 5432

        # postgresql to use psycopg2, posgresql+psycopg to use psycopg3
        url = URL.create(
            drivername="postgresql+psycopg",
            username=self._username,
            password=self._password,
            host=self._host,
            port=self._port,
            database=self._database,
        )

        self._engine = create_engine(url)

        self._session = sessionmaker(
            bind=self._engine, autoflush=False, autocommit=False
        )
    
    def create_engine(self) -> Engine:
        return self._engine
