import pytest
import project

def main():
    test_daily_average()
    test_sum_monthly()
    test_Calculator()

def test_sum_monthly():
    assert project.sum_monthly("profile1", 2024, 1) == 13122.0
    with pytest.raises(TypeError):
        project.sum_monthly(2)

def test_daily_average():
    _, average = project.daily_average("profile1", 2024, 1)
    assert average == 423.2903225806452
def test_Calculator():
    assert project.Calculator.add(1, 2, 1) == 3
    assert project.Calculator.subtract(1, 2, 1) == 1
    assert project.Calculator.divide(1, 3, 1) == 3
    assert project.Calculator.multiply(1, 1, 2) == 2
    