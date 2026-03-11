# test_employee/repository.py
# Unit tests for EmployeeRepository using MockSession returned by mock_session()
# employee_repo() returns EmployeeRepository with a MockSession

from python_labour_app.db.models import Employee
from python_labour_app.db.repositories import EmployeeRepository


def test_get_returns_employee_by_id(sqlite_session):
    employee: Employee = Employee(
        id=1, emp_no=42, is_active=True, first_name="Baba", last_name="Dook"
    )
    sqlite_session.add(employee)
    sqlite_session.commit()

    repo = EmployeeRepository(session=sqlite_session)
    result: Employee | None = repo.get(1)

    assert result == employee


def test_get_returns_none_if_id_not_exists(employee_repo, sqlite_session):
    employee: Employee = Employee(
        id=1, emp_no=42, is_active=True, first_name="Baba", last_name="Dook"
    )
    sqlite_session.add(employee)
    sqlite_session.commit()

    result: Employee = employee_repo.get(2)

    assert result is None


def test_get_all_returns_all_employees(employee_repo, sqlite_session):
    employees: list[Employee] = [
        Employee(
            id=1, emp_no=101, is_active=True, first_name="Natasha", last_name="Lisova"
        ),
        Employee(
            id=2, emp_no=102, is_active=True, first_name="Ramesh", last_name="Singla"
        ),
        Employee(
            id=3, emp_no=103, is_active=True, first_name="Nina", last_name="Rodriquez"
        ),
    ]

    # Add to database
    for employee in employees:
        sqlite_session.add(employee)

    sqlite_session.commit()

    result: list[Employee] = list(employee_repo.get_all())

    assert len(result) == 3
    assert result == employees


def test_get_all_returns_empty_when_no_employees(employee_repo, sqlite_session):
    result = list(employee_repo.get_all())

    assert result == []


def test_get_by_criteria_filters_employees(employee_repo, sqlite_session):
    employees = [
        Employee(
            id=1, emp_no=101, is_active=True, first_name="Alice", last_name="Smith"
        ),
        Employee(
            id=2, emp_no=102, is_active=False, first_name="Jason", last_name="Robertson"
        ),
    ]

    # Add to database.
    for employee in employees:
        sqlite_session.add(employee)
    sqlite_session.commit()

    criteria: dict = {"is_active": False}

    result: list[Employee] = list(employee_repo.get_by_criteria(criteria=criteria))

    assert len(result) == 1
    assert result == [employees[1]]
