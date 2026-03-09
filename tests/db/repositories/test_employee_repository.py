# test_employee/repository.py
# Unit tests for EmployeeRepository using MockSession returned by mock_session()
# employee_repo() returns EmployeeRepository with a MockSession

from python_labour_app.db.models.employee import Employee


def test_get_returns_employee_by_id(employee_repo, mock_session):
    employee: Employee = Employee(id=1, emp_no=42, first_name="Baba", last_name="Dook")
    mock_session.get_result = employee
    result: Employee = employee_repo.get(1)

    assert result == employee
