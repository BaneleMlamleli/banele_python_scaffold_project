import calculator


def test_addition():
    assert calculator.addition(3, 7) == 10


def test_multiplication():
    assert calculator.multiplication(3, 7) == 21


def test_subtraction():
    assert calculator.subtraction(23, 3) == 20


def test_division():
    assert calculator.division(10, 5) == 5
