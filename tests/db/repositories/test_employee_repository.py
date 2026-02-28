# test_employee_repository.py

from sqlalchemy.orm import Session


def test_employee_can_be_added(session: Session) -> None:
    emplo