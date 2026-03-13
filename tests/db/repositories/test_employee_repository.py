# test_employee/repository.py
# Unit tests for EmployeeRepository using MockSession returned by mock_session()
# employee_repo() returns EmployeeRepository with a MockSession
from python_labour_app.db.models import Employee
from python_labour_app.db.repositories import EmployeeRepository


def test_get_returns_employee_by_id(sqlite_session):
    employee: Employee = Employee(emp_no=42, first_name="Baba", last_name="Dook")
    sqlite_session.add(employee)
    sqlite_session.commit()

    repo: EmployeeRepository = EmployeeRepository(session=sqlite_session)
    result: Employee | None = repo.get(1)

    assert result == employee


def test_get_returns_none_if_id_not_exists(sqlite_session):
    employee: Employee = Employee(emp_no=42, first_name="Baba", last_name="Dook")
    sqlite_session.add(employee)
    sqlite_session.commit()

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

    sqlite_session.commit()

    repo: EmployeeRepository = EmployeeRepository(session=sqlite_session)
    result: list[Employee] = repo.get_all()

    assert len(result) == 3
    assert result == employees


def test_get_all_returns_empty_when_no_employees(sqlite_session):
    repo: EmployeeRepository = EmployeeRepository(session=sqlite_session)
    result = list(repo.get_all())

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
    sqlite_session.commit()

    criteria: dict = {"is_active": False}

    repo: EmployeeRepository = EmployeeRepository(session=sqlite_session)
    result: list[Employee] = list(repo.get_by_criteria(criteria=criteria))

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
    sqlite_session.commit()

    criteria: dict = {"first_name": "Jorja", "last_name": "Andrews"}

    repo: EmployeeRepository = EmployeeRepository(session=sqlite_session)
    result: list[Employee] = list(repo.get_by_criteria(criteria=criteria))

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
    sqlite_session.commit()

    criteria: dict = {"first_name": "Mitsuki", "is_active": True}

    repo: EmployeeRepository = EmployeeRepository(session=sqlite_session)
    result: list[Employee] = list(repo.get_by_criteria(criteria=criteria))

    assert result == []


def test_add_persists_employee(sqlite_session):
    employee_details: dict = {"emp_no": 10, "first_name": "Jorja", "last_name": "Andrews"}

    repo: EmployeeRepository = EmployeeRepository(session=sqlite_session)
    result: Employee | None = repo.add(**employee_details)
    sqlite_session.flush()

    assert isinstance(result, Employee)
    assert result.emp_no == employee_details["emp_no"]
    assert result.first_name == employee_details["first_name"]
    assert result.last_name == employee_details["last_name"]
