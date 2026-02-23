# test_sqlite_factory.py
from sqlalchemy.engine import Engine

from python_labour_app.db.factories.sqlite_factory import SQLiteFactory


def test_sqlite_factory_creates_engine() -> None:
    factory = SQLiteFactory(url="sqlite+pysqlite:///test.db")
    engine = factory.create_engine()

    assert isinstance(engine, Engine)
    assert "sqlite" in str(engine.url)
