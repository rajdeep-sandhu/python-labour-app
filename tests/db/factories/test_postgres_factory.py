# test_postgres_factory.py
from sqlalchemy import Engine
from sqlalchemy.orm import Session

from python_labour_app.db.factories import PostgresFactory


def test_postgres_factory_creates_engine() -> None:
    factory: PostgresFactory = PostgresFactory()
    engine: Engine = factory.create_engine()

    assert isinstance(engine, Engine)
    assert "postgresql" in str(engine.url)
    assert engine.url.drivername.startswith("postgresql")


def test_postgres_factory_creates_session() -> None:
    factory: PostgresFactory = PostgresFactory()
    session: Session = factory.create_session()

    assert isinstance(session, Session)
    session.close()
