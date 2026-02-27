# employee_repository.py

from sqlalchemy.orm import Session


class EmployeeRepository:
    def __init__(self, session: Session) -> None:
        self._session = session
