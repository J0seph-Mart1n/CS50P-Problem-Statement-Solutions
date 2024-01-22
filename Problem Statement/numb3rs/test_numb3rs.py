from numb3rs import validate

def test_assert():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("cat") == False
    assert validate("1.2.3.4") == True
    assert validate("11.22.33.44") == True
    assert validate("64.128.256.512") == False
    assert validate("249.249.249.249") == True

