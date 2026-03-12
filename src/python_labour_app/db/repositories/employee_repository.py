# employee_repository.py
from typing import Generator, Iterator

from sqlalchemy import Select, select
from sqlalchemy.orm import Session

from python_labour_app.db.models import Employee
from python_labour_app.db.repositories import Repository


class EmployeeRepository(Repository[Employee]):
    def __init__(self, session: Session) -> None:
        self._session = session

    def get(self, id: int) -> Employee | None:
        """
        Get an employee by id.

        Returns None if does not exist.
        """
        employee: Employee | None = self._session.get(Employee, id)
        return employee

    def get_all(self) -> Generator[Employee, None, None]:
        """Get all employees."""
        query = select(Employee)
        result: Iterator[Employee] = self._session.scalars(query)

        yield from result

    def get_by_criteria(
        self, criteria: dict[str, object]
    ) -> Generator[Employee, None, None]:
        """Get employees by criteria."""
        query: Select = select(Employee)

        for field, value in criteria.items():
            if not hasattr(Employee, field):
                raise ValueError(f"Invalid filter criteria field: {field}.")
            query = query.where(getattr(Employee, field) == value)

        result: Iterator[Employee] = self._session.scalars(query)
        yield from result

    def add(self, **kwargs: dict[str, object]) -> Employee | None:
        """Add an employee."""
        employee: Employee = Employee(**kwargs)
        self._session.add(employee)
        return employee

    def update(self, id: int, **kwargs: dict[str, object]) -> None:
        """Update an employee."""
        raise NotImplementedError

    def delete(self, id: int) -> None:
        """Delete an employee."""
        raise NotImplementedError
