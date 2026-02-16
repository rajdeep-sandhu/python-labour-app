# All models import from the same Base.
# Allows separation of concerns, scaling and prevents circular imports.

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass
