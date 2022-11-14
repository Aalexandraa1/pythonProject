import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator()

    def test_multiply_success(self):
        assert self.calc.multiply(2, 3) == 6

    def test_division_success(self):
        assert self.calc.division(4, 2) == 2

    def test_subtraction_success(self):
        assert self.calc.subtraction(3, 1) == 2

    def test_adding_success(self):
        assert self.calc.adding(2, 2) == 2

    def teardown(self):
        print('Выполнение метода Teardown')