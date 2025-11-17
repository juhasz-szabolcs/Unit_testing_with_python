import pytest
from calculator import sum, subtract, multiply, divide

def test_sum():
    assert sum(2, 3) == 5
    assert sum(-2, 3) == 1
    assert sum(-2, -3) == -5
    assert sum(-2, 0) == -2

def test_subtract():
    assert subtract(3, 2) == 1
    assert subtract(-2, 3) == -5
    assert subtract(-2, -3) == 1
    assert subtract(-2, 0) == -2

def test_multiply():
    assert multiply(2,3) == 6
    assert multiply(-2,3) == -6
    assert multiply(-2,-3) == 6
    assert multiply(-2,0) == 0

def test_divide():
    assert divide(6,2) == 3
    assert divide(-6,2) == -3
    assert divide(-6,-2) == 3
    assert divide(6,0) == "Error: Division by zeroe"






# python -m pytest test_calculator.py -v 