# repositories/conftest.py
from typing import Self

import pytest

from python_labour_app.db.repositories import EmployeeRepository


@pytest.fixture
def mock_session(monkeypatch):
    """Create a mock session object."""

    class MockSession:
        def __init__(self) -> None:
            self.added = []
            self.committed = False
            self.deleted = []
            self.get_results = {}
            self.scalar_result = None
            self.execute_result = None
            self.query_result = None
            self.filter_result = None
            self.first_result = None
            self.all_result = None

        def get(self, model, id_):
            """
            Return object for the specified model and id_.

            Return None if id_ does not exist.
            """
            return self.get_results.get(model, {}).get(id_)

        def filter(self, condition) -> Self:
            self.filter_result = condition
            return self

        def first(self):
            return self.first_result

        def all(self):
            return self.all_result

        def add(self, obj):
            self.added.append(obj)

        def commit(self):
            self.committed = True

        def delete(self, obj):
            self.deleted.append(obj)

    return MockSession()


@pytest.fixture
def employee_repo(mock_session) -> EmployeeRepository:
    """Create an EmployeeRepository with mock session."""
    return EmployeeRepository(session=mock_session)
