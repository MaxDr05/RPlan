import pytest


class calculator():
    def mul(self,a,b):
        return a*b

    def div(self,a,b):
        if b == 0:
            raise ValueError('b is 0')
        return a/b

class Test_calculator():
    def setup_method(self):
        self.calculator = calculator()

    def teardown_method(self):
        del self.calculator

    def test_mul(self):
        assert self.calculator.mul(0,2) == 0
        assert self.calculator.mul(1,2) == 2
        assert self.calculator.mul(2,2) == 4
        assert self.calculator.mul(3,-2) == -6

    def test_div(self):
        assert self.calculator.div(0,2) == 0
        assert self.calculator.div(1,2) == 0.5
        assert self.calculator.div(2,2) == 1

    def test_divByZero(self):
        with pytest.raises(ValueError,match='b is 0'):
            self.calculator.div(1,0)
