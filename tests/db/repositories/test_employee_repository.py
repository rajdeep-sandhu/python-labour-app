# test_employee/repository.py
# Unit tests for EmployeeRepository

from python_labour_app.db.models.employee import Employee


def test_get_returns_employee_by_id(self, employee_repo, mock_session):
    employee = Employee(id=1, emp_no=42, first_name="Baba", last_name="Dook")
    mock_session.first_result = employee

    assert employee_repo.get(1) == employee
