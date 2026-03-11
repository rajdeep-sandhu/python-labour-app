import pytest
from sqlalchemy.exc import IntegrityError

from python_labour_app.db.models import Employee


def test_employee_persists(sqlite_session):
    employee: Employee = Employee(first_name="John", last_name="Doe")
    sqlite_session.add(employee)
    sqlite_session.commit()
    sqlite_session.refresh(employee)

    assert employee.id is not None
    assert employee.emp_no is None
    assert employee.is_active is True


def test_employee_requires_first_name(sqlite_session) -> None:
    employee: Employee = Employee(last_name="Doe")
    sqlite_session.add(employee)

    with pytest.raises(IntegrityError):
        sqlite_session.commit()


def test_employee_requires_last_name(sqlite_session) -> None:
    employee: Employee = Employee(first_name="John")
    sqlite_session.add(employee)

    with pytest.raises(IntegrityError):
        sqlite_session.commit()


def test_emp_no_unique_constraint(sqlite_session) -> None:
    employee_1: Employee = Employee(first_name="John", last_name="Doe", emp_no=5)
    employee_2: Employee = Employee(first_name="Ruchika", last_name="Yashpal", emp_no=5)
    sqlite_session.add_all([employee_1, employee_2])

    with pytest.raises(IntegrityError):
        sqlite_session.commit()


def test_employee_can_be_deactivated(sqlite_session) -> None:
    employee: Employee = Employee(first_name="Amrik", last_name="Singh")
    sqlite_session.add(employee)
    sqlite_session.commit()

    employee.is_active = False
    sqlite_session.commit()
    sqlite_session.refresh(employee)

    assert employee.is_active is False
