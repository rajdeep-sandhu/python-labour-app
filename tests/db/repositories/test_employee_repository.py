# test_employee/repository.py
# Unit tests for EmployeeRepository using MockSession returned by mock_session()
# employee_repo() returns EmployeeRepository with a MockSession
import pytest

from python_labour_app.db.models import Employee
from python_labour_app.db.repositories import EmployeeRepository


def test_get_returns_employee_by_id(sqlite_session):
    employee: Employee = Employee(emp_no=42, first_name="Baba", last_name="Dook")
    sqlite_session.add(employee)
    sqlite_session.flush()

    repo: EmployeeRepository = EmployeeRepository(session=sqlite_session)
    result: Employee | None = repo.get(1)

    assert result == employee


def test_get_returns_none_if_id_not_exists(sqlite_session):
    employee: Employee = Employee(emp_no=42, first_name="Baba", last_name="Dook")
    sqlite_session.add(employee)
    sqlite_session.flush()

    repo: EmployeeRepository = EmployeeRepository(session=sqlite_session)
    result: Employee | None = repo.get(2)

    assert result is None


def test_get_all_returns_all_employees(sqlite_session):
    employees: list[Employee] = [
        Employee(emp_no=101, first_name="Natasha", last_name="Lisova"),
        Employee(emp_no=102, first_name="Ramesh", last_name="Singla"),
        Employee(emp_no=103, first_name="Nina", last_name="Rodriquez"),
    ]

    # Add to database
    for employee in employees:
        sqlite_session.add(employee)

    sqlite_session.flush()

    repo: EmployeeRepository = EmployeeRepository(session=sqlite_session)
    result: list[Employee] = repo.get_all()

    assert len(result) == 3
    assert result == employees


def test_get_all_returns_empty_when_no_employees(sqlite_session):
    repo: EmployeeRepository = EmployeeRepository(session=sqlite_session)
    result = repo.get_all()

    assert result == []


def test_get_by_criteria_filters_employees(sqlite_session):
    employees: list[Employee] = [
        Employee(emp_no=101, first_name="Alice", last_name="Smith"),
        Employee(
            emp_no=102, is_active=False, first_name="Jason", last_name="Robertson"
        ),
    ]

    # Add to database.
    for employee in employees:
        sqlite_session.add(employee)
    sqlite_session.flush()

    criteria: dict = {"is_active": False}

    repo: EmployeeRepository = EmployeeRepository(session=sqlite_session)
    result: list[Employee] = repo.get_by_criteria(criteria=criteria)

    assert len(result) == 1
    assert result == [employees[1]]


def test_get_by_criteria_multiple_criteria(sqlite_session):
    employees: list[Employee] = [
        Employee(emp_no=10, first_name="Jorja", last_name="Andrews"),
        Employee(emp_no=11, first_name="Callum", last_name="Baker"),
        Employee(
            emp_no=12,
            is_active=False,
            first_name="Jorja",
            middle_names="Cristina",
            last_name="Andrews",
        ),
    ]

    # Add to database.
    for employee in employees:
        sqlite_session.add(employee)
    sqlite_session.flush()

    criteria: dict = {"first_name": "Jorja", "last_name": "Andrews"}

    repo: EmployeeRepository = EmployeeRepository(session=sqlite_session)
    result: list[Employee] = repo.get_by_criteria(criteria=criteria)

    assert len(result) == 2
    assert result == [employees[0], employees[2]]


def test_get_by_criteria_returns_empty_if_not_found(sqlite_session):
    employees: list[Employee] = [
        Employee(emp_no=10, first_name="Jorja", last_name="Andrews"),
        Employee(emp_no=11, first_name="Callum", last_name="Baker"),
        Employee(
            emp_no=12,
            is_active=False,
            first_name="Jorja",
            middle_names="Cristina",
            last_name="Smith",
        ),
    ]

    # Add to database.
    for employee in employees:
        sqlite_session.add(employee)
    sqlite_session.flush()

    criteria: dict = {"first_name": "Mitsuki", "is_active": True}

    repo: EmployeeRepository = EmployeeRepository(session=sqlite_session)
    result: list[Employee] = repo.get_by_criteria(criteria=criteria)

    assert result == []


def test_add_persists_employee(sqlite_session):
    employee: Employee = Employee(emp_no=10, first_name="Jorja", last_name="Andrews")

    repo: EmployeeRepository = EmployeeRepository(session=sqlite_session)
    result: Employee | None = repo.add(employee)
    sqlite_session.flush()

    assert isinstance(result, Employee)
    assert result.emp_no == employee.emp_no
    assert result.first_name == employee.first_name
    assert result.last_name == employee.last_name


def test_add_multiple_employees(sqlite_session):
    employees: list[Employee] = [
        Employee(emp_no=101, first_name="Natasha", last_name="Lisova"),
        Employee(emp_no=102, first_name="Ramesh", last_name="Singla"),
        Employee(emp_no=103, first_name="Nina", last_name="Rodriquez"),
    ]

    # Add to database.
    repo: EmployeeRepository = EmployeeRepository(session=sqlite_session)
    results: list[Employee] = [repo.add(employee) for employee in employees]
    sqlite_session.flush()

    assert results == employees


def test_update_employee(sqlite_session):
    employee: Employee = Employee(emp_no=101, first_name="Natasha", last_name="Lisova")
    sqlite_session.add(employee)
    sqlite_session.flush()

    employee.first_name = "Hristina"

    # Update database
    repo: EmployeeRepository = EmployeeRepository(session=sqlite_session)
    result: Employee | None = repo.update(employee)

    assert result == employee


def test_update_raises_when_id_is_none(sqlite_session):
    employee: Employee = Employee(emp_no=101, first_name="Natasha", last_name="Lisova")
    sqlite_session.add(employee)
    sqlite_session.flush()

    emp_updated: Employee = Employee(
        emp_no=101, first_name="Hristina", last_name="Lisova"
    )

    # Update database
    repo: EmployeeRepository = EmployeeRepository(session=sqlite_session)

    with pytest.raises(ValueError):
        repo.update(emp_updated)


def test_delete_employee(sqlite_session):
    employee: Employee = Employee(emp_no=101, first_name="Natasha", last_name="Lisova")
    sqlite_session.add(employee)
    sqlite_session.flush()

    # Delete from database
    repo: EmployeeRepository = EmployeeRepository(session=sqlite_session)
    repo.delete(employee)
    sqlite_session.flush()

    result: Employee | None = sqlite_session.get(Employee, employee.id)

    assert result is None
