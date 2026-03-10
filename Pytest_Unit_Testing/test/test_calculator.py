from Pytest_Unit_Testing.src.calculator import Calculator



def test_add():
    calc = Calculator()
    assert calc.add(1, 2) == 3
    assert calc.add(1, -1) == 0
    assert calc.add(-1, -1) == -2


def test_subtract():
    calc = Calculator()
    assert calc.subtract(1, 2) == -1
    assert calc.subtract(1, -1) == 2
    assert calc.subtract(2, 1) == 1
    assert calc.subtract(1, 1) == 0


def test_multiply():
    calc = Calculator()
    assert calc.multiply(1, 2) == 2
    assert calc.multiply(1, -1) == -1
    assert calc.multiply(2, 0) == 0
    assert calc.multiply(-1, -1) == 1


def test_divide():
    calc = Calculator()
    assert calc.divide(6, 2) == 3
    assert calc.divide(-1, 1) == -1
    assert calc.divide(-1, -1) == 1

    try:
        calc.divide(1, 0)
    except ValueError as e:
        print(f"Caught an error: {e}")