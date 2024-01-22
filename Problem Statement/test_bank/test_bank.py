from bank import value

def test_assert():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("hey") == 20
    assert value("HEY") == 20
    assert value("what up") == 100
    assert value("WHAT UP") == 100
