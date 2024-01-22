from plates import is_valid

def test_assert():
    assert is_valid("123") == False
    assert is_valid("OUTATIME") == False
    assert is_valid("CS50P2") == False
    assert is_valid("CS05") == False
    assert is_valid("PI3.14") == False
    assert is_valid("H") == False

