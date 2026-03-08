# repositories/conftest.py
import pytest


@pytest.fixture
def mock_session(monkeypatch) -> None:
    """Create a mock session object."""
    class MockSession:
        raise NotImplementedError
    