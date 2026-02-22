from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from . import Base


class Employee(Base):
    """
    Represents an employee.
    emp_no may initially be NULL and cannot be changed once assigned.
    id is used as the internal immutable primary key
    Employees can only be deactivated, not deleted.
    """

    __tablename__ = "employees"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    emp_no: Mapped[int] = mapped_column(Integer, nullable=True, unique=True)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    middle_names: Mapped[str] = mapped_column(String(100), nullable=True)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
