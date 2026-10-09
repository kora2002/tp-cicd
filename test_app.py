from app import addition, soustraction


def test_addition():
    assert addition(2, 3) == 5


def test_addition_zero():
    assert addition(10, 0) == 10


def test_soustraction():
    assert soustraction(10, 3) == 7