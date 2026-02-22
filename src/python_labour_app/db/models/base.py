from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    All models import from the same Base.
    Allows separation of concerns, scaling and prevents circular imports.
    """
    pass
