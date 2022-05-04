import pytest_check as check


def add_numbers(number1: float, number2: float) -> float:
    return number1 + number2


def test_add_numbers():
    check.equal(add_numbers(1, 2), 3)
    check.equal(add_numbers(1, -2), -1)
    check.equal(add_numbers(1.1, -2.1), -1.0)
