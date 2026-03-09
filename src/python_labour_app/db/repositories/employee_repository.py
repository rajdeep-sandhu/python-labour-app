# employee_repository.py
from typing import Generator

from sqlalchemy.orm import Session

from python_labour_app.db.models import Employee
from python_labour_app.db.repositories.repository import Repository


class EmployeeRepository(Repository):
    def __init__(self, session: Session) -> None:
        self._session = session

    def get(self, id: int) -> Employee | None:
        """Get an employee by id."""
        employee: Employee | None = self._session.get(Employee, id)
        return employee

    def get_all(self) -> Generator[Employee, None, None]:
        """Get all items."""
        raise NotImplementedError

    def get_by_criteria(
        self, criteria: dict[str, object]
    ) -> Generator[Employee, None, None]:
        """Get items by criteria."""
        raise NotImplementedError

    def add(self, **kwargs: dict[str, object]) -> None:
        """Add an employee."""
        raise NotImplementedError
