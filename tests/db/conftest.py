from typing import Generator

import pytest
from sqlalchemy import Connection, Engine, RootTransaction, create_engine, event
from sqlalchemy.orm import Session, sessionmaker

from python_labour_app.db.models import Base


@pytest.fixture(scope="session")
def engine() -> Generator[Engine, None, None]:
    """Setup engine and metadata for the test session."""
    url = "sqlite+pysqlite:///test.db"
    engine = create_engine(url)

    # Setup: Create tables.
    Base.metadata.create_all(bind=engine)

    yield engine

    # Teardown: Drop tables.
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def sqlite_session(engine) -> Generator[Session, None, None]:
    """Setup and yield a Session for the test session."""

    # Setup
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    SessionLocal: sessionmaker = sessionmaker(bind=engine)
    session: Session = SessionLocal()

    yield session

    # Teardown
    session.close()
