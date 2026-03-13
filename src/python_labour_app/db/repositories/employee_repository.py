# employee_repository.py
from sqlalchemy import ScalarResult, Select, select
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

    def get_all(self) -> list[Employee]:
        """Get all employees."""
        query = select(Employee)
        result: ScalarResult[Employee] = self._session.scalars(query)

        return list(result)

    def get_by_criteria(self, criteria: dict[str, object]) -> list[Employee]:
        """Get employees by criteria."""
        query: Select = select(Employee)

        for field, value in criteria.items():
            if not hasattr(Employee, field):
                raise ValueError(f"Invalid filter criteria field: {field}.")
            query = query.where(getattr(Employee, field) == value)

        result: ScalarResult[Employee] = self._session.scalars(query)

        return list(result)

    def add(self, entity: Employee) -> Employee | None:
        """Add an employee."""
        self._session.add(entity)
        return entity

    def update(self, entity: Employee) -> None:
        """Update an employee."""
        raise NotImplementedError

    def delete(self, entity: Employee) -> None:
        """Delete an employee."""
        raise NotImplementedError
