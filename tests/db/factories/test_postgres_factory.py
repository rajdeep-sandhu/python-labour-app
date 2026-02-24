# test_postgres_factory.py
from sqlalchemy import Engine

from python_labour_app.db.factories import PostgresFactory


def test_postgres_factory_creates_engine() -> None:
    factory: PostgresFactory = PostgresFactory()
    engine: Engine = factory.create_engine()

    assert isinstance(engine, Engine)
    assert "postgresql" in str(engine.url)
    assert engine.url.drivername.startswith("postgresql")
