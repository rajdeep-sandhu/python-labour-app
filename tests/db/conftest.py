import pytest
from sqlalchemy.orm import Session

from python_labour_app.db.models import Base
from python_labour_app.db.sqlite_factory import SQLiteFactory


@pytest.fixture(scope="session")
def sqlite_factory() -> SQLiteFactory:
    """Return SQLiteFactory for a test database."""
    return SQLiteFactory(url="sqlite+pysqlite:///test.db")


@pytest.fixture(scope="session")
def engine(sqlite_factory: SQLiteFactory):
    """Setup engine and metadata for the test session."""
    engine = sqlite_factory.create_engine()

    # Setup: Create tables.
    Base.metadata.create_all(bind=engine)

    yield

    # Teardown: Drop tables.
    Base.metadata.drop_all(bind=engine)
