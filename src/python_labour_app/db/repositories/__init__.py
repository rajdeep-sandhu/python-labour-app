# db/repositories/__init__.py
from .employee_repository import EmployeeRepository
from .repository import Repository

__all__ = ["Repository", "EmployeeRepository"]
