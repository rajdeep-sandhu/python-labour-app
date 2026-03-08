# repositories/conftest.py
import pytest


@pytest.fixture
def mock_session(monkeypatch) -> None:
    """Create a mock session object."""
    class MockSession:
        def __init__(self) -> None:
            self.added = []
            self.committed = False
            self.deleted = []
            self.query_result = None
            self.filter_result = None
            self.first_result = None
            self.all_result = None
    