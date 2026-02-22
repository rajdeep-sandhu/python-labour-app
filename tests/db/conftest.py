from typing import Generator

import pytest
from sqlalchemy import Connection, Engine, RootTransaction
from sqlalchemy.orm import Session, sessionmaker

from python_labour_app.db.models import Base
from python_labour_app.db.sqlite_factory import SQLiteFactory


@pytest.fixture(scope="session")
def sqlite_factory() -> SQLiteFactory:
    """Return SQLiteFactory for a test database."""
    return SQLiteFactory(url="sqlite+pysqlite:///test.db")


@pytest.fixture(scope="session")
def engine(sqlite_factory: SQLiteFactory) -> Generator[Engine, None, None]:
    """Setup engine and metadata for the test session."""
    engine: Engine = sqlite_factory.create_engine()

    # Setup: Create tables.
    Base.metadata.create_all(bind=engine)

    yield engine

    # Teardown: Drop tables.
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def session(engine) -> Generator[Session, None, None]:
    """Setup and yield a Session for the test session."""

    # Setup
    connection: Connection = engine.connect()
    transaction: RootTransaction = connection.begin()
    SessionLocal: sessionmaker[Session] = sessionmaker(
        bind=connection, autoflush=False, autocommit=False
    )
    session: Session = SessionLocal()

    yield session

    # Teardown
    session.close()
    transaction.rollback()
    connection.close()
