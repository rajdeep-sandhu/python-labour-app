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
def session(engine) -> Generator[Session, None, None]:
    """Setup and yield a Session for the test session."""

    # Setup
    connection: Connection = engine.connect()
    transaction: RootTransaction = connection.begin()
    SessionLocal: sessionmaker[Session] = sessionmaker(
        bind=connection, autoflush=False, autocommit=False
    )
    session: Session = SessionLocal()

    # For proper test isolation, start a nested transaction (SAVEPOINT).
    # The outer connection.begin() is never committed.
    # Each session.commit() operates on this SAVEPOINT.
    # On a failing commit (e.g. IntegrityError), only the SAVEPOINT is rolled back.
    # The outer transaction is left active, ensuring the session remains usable,
    # and teardown rollback succeeds without deassociated transaction warnings.
    session.begin_nested()

    @event.listens_for(session, "after_transaction_end")
    def restart_savepoint(sess: Session, trans) -> None:
        if trans.nested and not trans._parent.nested:
            sess.begin_nested()

    yield session

    # Teardown
    session.close()
    transaction.rollback()
    connection.close()
