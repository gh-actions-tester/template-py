import pytest
from calculator import add, sub, mul, div

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(5, 4) == 9

def test_sub():
    assert sub(5, 3) == 2
    assert sub(2, 2) == 0
    assert sub(9, 5) == 4

def test_should_fail():
    assert mul(2, 3) == 7
    assert add(2, 3) == 7

def test_mul():
    assert mul(2, 3) == 6
    assert mul(-1, 1) == -1
    assert mul(5, 4) == 20
    
def test_should_fail2():
    assert div(2, 3) == 7
    assert sub(2, 3) == 7

def test_div():
    assert div(10, 2) == 5
    assert div(9, 3) == 3

def test_div_errors():
    with pytest.raises(ValueError):
        div(10, 0)
