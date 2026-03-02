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
        """Add employee, increment id, set as active."""
        if employee.id is None:
            employee.id = self._next_id
            self._next_id += 1

        if employee.is_active is None:
            employee.is_active = True

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

    # Add employees
    repo.add(Employee(emp_no=1, first_name="Natalia", last_name="Chavez"))
    repo.add(
        Employee(emp_no=76, first_name="Ana", middle_names="C", last_name="Dateshidze")
    )
    repo.add(Employee(emp_no=77, first_name="Alejandro", last_name="Chavez"))
    print(repo.employees, "\n")

    # Get employees
    print(repr(repo.get(0)), "\n")

    print("get_all()")
    for employee in repo.get_all():
        print(repr(employee))

    print("\nget_by_criteria()")
    criteria: dict[str, object] = {"last_name": "Chavez"}
    for employee in repo.get_by_criteria(criteria=criteria):
        print(repr(employee))

    # Update employee
    repo.update(Employee(id=0, emp_no=1, first_name="Cristina", last_name="Chavez"))
    print("\nupdate()")
    print(repr(repo.get(0)))

    # Delete employee
    emp_to_delete = repo.get(0)
    print(f"\nDelete: {repr(emp_to_delete)}")
    repo.delete(emp_to_delete)

    print("After deletion:")
    for employee in repo.get_all():
        print(repr(employee))


if __name__ == "__main__":
    main()
