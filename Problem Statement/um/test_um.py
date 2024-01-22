from um import count

def test_um():
    assert count("um") == True
    assert count(", um,") == True
    assert count("UM") == True
    assert count("yummy") == False
