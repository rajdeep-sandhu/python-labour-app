# mock_employee_repository.py

from typing import Generator, Optional

from python_labour_app.db.models.employee import Employee
from python_labour_app.db.repositories.repository import Repository


class MockEmployeeRepository(Repository[Employee]):
    def __init__(self, employees: Optional[dict[int, Employee]] = None):
        self.employees = employees or {}

    def get(self, id_: int) -> Employee:
        return self.employees[id_]

    def get_all(self) -> Generator[Employee, None, None]:
        yield from self.employees.values()

    def add(self, employee: Employee) -> None:
        self.employees[len(self.employees)] = employee

    def update(self, employee: Employee) -> None:
        if employee.id is None:
            raise ValueError("Cannot update an Employee without an id.")
        
        self.employees[employee.id] = employee