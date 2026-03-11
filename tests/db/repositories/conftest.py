# repositories/conftest.py
from typing import Self

import pytest


@pytest.fixture
def mock_session(monkeypatch):
    """Create a mock session object."""

    class MockSession:
        def __init__(self) -> None:
            self.added = []
            self.committed = False
            self.deleted = []
            self.get_results = {}
            self.scalars_result = None
            self.execute_result = None

        def get(self, model, id_):
            """
            Return object for the specified model and id_.

            Return None if id_ does not exist.
            """
            return self.get_results.get(model, {}).get(id_)

        def scalars(self, query):
            """Return scalars result."""
            return self.scalars_result if self.scalars_result is not None else iter([])

        def execute(self, query):
            """Return result for query execute."""
            return self.execute_result

        def add(self, obj):
            self.added.append(obj)

        def commit(self):
            self.committed = True

        def delete(self, obj):
            self.deleted.append(obj)

    return MockSession()
