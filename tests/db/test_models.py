import pytest
from sqlalchemy.exc import IntegrityError

from python_labour_app.db.models import Employee


def test_employee_persists(session):
    employee: Employee = Employee(first_name="John", last_name="Doe")
    session.add(employee)
    session.commit()
    session.refresh(employee)

    assert employee.id is not None
    assert employee.emp_no is None
    assert employee.is_active is True


def test_employee_requires_first_name(session) -> None:
    employee: Employee = Employee(last_name="Doe")
    session.add(employee)

    with pytest.raises(IntegrityError):
        session.commit()


def test_employee_requires_last_name(session) -> None:
    employee: Employee = Employee(first_name="John")
    session.add(employee)

    with pytest.raises(IntegrityError):
        session.commit()


def test_emp_no_unique_constraint(session) -> None:
    employee_1: Employee = Employee(first_name="John", last_name="Doe", emp_no=5)
    employee_2: Employee = Employee(first_name="Ruchika", last_name="Yashpal", emp_no=5)
    session.add_all([employee_1, employee_2])

    with pytest.raises(IntegrityError):
        session.commit()
