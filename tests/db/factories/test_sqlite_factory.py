# test_sqlite_factory.py
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from python_labour_app.db.factories.sqlite_factory import SQLiteFactory


def test_sqlite_factory_creates_engine() -> None:
    factory: SQLiteFactory = SQLiteFactory(url="sqlite+pysqlite:///test.db")
    engine: Engine = factory.create_engine()

    assert isinstance(engine, Engine)
    assert "sqlite" in str(engine.url)
    assert engine.url.drivername.startswith("sqlite")


def test_sqlite_factory_creates_session() -> None:
    factory: SQLiteFactory = SQLiteFactory(url="sqlite+pysqlite:///test.db")
    session: Session = factory.create_session()

    assert isinstance(session, Session)
    session.close()
