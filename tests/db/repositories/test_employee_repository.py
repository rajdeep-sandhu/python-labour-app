# test_employee/repository.py
# Unit tests for EmployeeRepository using MockSession returned by mock_session()
# employee_repo() returns EmployeeRepository with a MockSession

from python_labour_app.db.models.employee import Employee


def test_get_returns_employee_by_id(employee_repo, sqlite_session):
    employee: Employee = Employee(
        id=1, emp_no=42, is_active=True, first_name="Baba", last_name="Dook"
    )
    sqlite_session.add(employee)
    sqlite_session.commit()

    result: Employee = employee_repo.get(1)

    assert result == employee


def test_get_returns_none_if_id_not_exists(employee_repo, sqlite_session):
    employee: Employee = Employee(
        id=1, emp_no=42, is_active=True, first_name="Baba", last_name="Dook"
    )
    sqlite_session.add(employee)
    sqlite_session.commit()

    result: Employee = employee_repo.get(2)

    assert result is None


def test_get_all_returns_all_employees(employee_repo, mock_session):
    emp1: Employee = Employee(
        id=1, emp_no=101, is_active=True, first_name="Natasha", last_name="Yulianova"
    )
    emp2: Employee = Employee(
        id=2, emp_no=102, is_active=True, first_name="Ramesh", last_name="Singla"
    )
    emp3: Employee = Employee(
        id=3, emp_no=103, is_active=True, first_name="Nina", last_name="Rodriquez"
    )

    mock_session.scalars_result = iter([emp1, emp2, emp3])
    result = list(employee_repo.get_all())

    assert len(result) == 3
    assert result == [emp1, emp2, emp3]


def test_get_all_returns_empty_when_no_employees(employee_repo, mock_session):
    result = list(employee_repo.get_all())

    assert result == []


def test_get_by_criteria_filters_employees(employee_repo, mock_session):
    emp1: Employee = Employee(
        id=1, emp_no=101, is_active=True, first_name="Alice", last_name="Smith"
    )
    emp2: Employee = Employee(
        id=2, emp_no=102, is_active=False, first_name="Jason", last_name="Robertson"
    )

    criteria: dict = {"is_active": False}

    mock_session.scalars_result = iter([emp1, emp2])
    result: list[Employee] = list(employee_repo.get_by_criteria(criteria=criteria))

    assert len(result) == 1
    assert result == [emp2]
