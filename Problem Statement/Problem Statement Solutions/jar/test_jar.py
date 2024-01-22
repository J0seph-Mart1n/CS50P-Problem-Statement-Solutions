from jar import Jar
import pytest

def test_init():
    jar = Jar()

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(20)
    jar.deposit(10)
    assert jar.size == 10
    with pytest.raises(ValueError):
        jar.deposit(20)


def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(2)
    assert jar.size==8
    with pytest.raises(ValueError):
        jar.withdraw(50)

