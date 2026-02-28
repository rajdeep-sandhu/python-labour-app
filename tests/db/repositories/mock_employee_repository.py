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
