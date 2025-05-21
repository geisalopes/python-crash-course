import pytest
from employee import Employee


@pytest.fixture
def sample_employee():
    return Employee("Geisa", "Lopes", 7000)


def test_give_default_raise():
    # criar instância de Employee com salario de 5000
    emp = Employee("Geisa", "Lopes", 5000)
    # aplicar o aumento
    emp.give_raise()
    # verificar se o salário aumentou 5000
    assert emp.annual_salary == 10000


def test_give_custom_raise():
    # criar instância de Employee
    emp = Employee("Geisa", "Lopes", 5000)
    # aplicar um aumento personalizado (ex: 10000)
    emp.give_raise(10000)
    # verificar se o salário aumentou corretamente
    assert emp.annual_salary == 15000
