# mock_employee_repository.py

from typing import Generator, Optional

from python_labour_app.db.models.employee import Employee
from python_labour_app.db.repositories.repository import Repository


class MockEmployeeRepository(Repository[Employee]):
    def __init__(self, employees: Optional[dict[int, Employee]] = None):
        self.employees = employees or {}
        self._next_id = 0

    def get(self, id_: int) -> Employee:
        return self.employees[id_]

    def get_all(self) -> Generator[Employee, None, None]:
        yield from self.employees.values()

    def get_by_criteria(
        self, criteria: dict[str, object]
    ) -> Generator[Employee, None, None]:
        # Iterate through employees.
        for employee in self.employees.values():
            # Yield employee if all criteria values match.
            if all(
                (getattr(employee, field, None) == value)
                for field, value in criteria.items()
            ):
                yield employee

    def add(self, employee: Employee) -> None:
        if employee.id is None:
            employee.id = self._next_id
            self._next_id += 1
        self.employees[len(self.employees)] = employee

    def update(self, employee: Employee) -> None:
        if employee.id is None:
            raise ValueError("Cannot update an Employee without an id.")

        self.employees[employee.id] = employee

    def delete(self, employee: Employee) -> None:
        if employee.id is None:
            raise ValueError("Cannot delete an Employee without an id.")

        del self.employees[employee.id]


def main():
    repo = MockEmployeeRepository()
    repo.add(Employee(emp_no=1, first_name="Natalia", last_name="Chavez"))
    repo.add(Employee(emp_no=76, first_name="Ana", last_name="Dateshidze"))
    print(repo.employees, "\n")

    print(repr(repo.get(0)), "\n")

    for e in repo.get_all():
        print(repr(e))


if __name__ == "__main__":
    main()
