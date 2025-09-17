import pytest
from factorial import factorial

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120

def test_factorial_negative():
    import pytest
    with pytest.raises(ValueError):
        factorial(-1)