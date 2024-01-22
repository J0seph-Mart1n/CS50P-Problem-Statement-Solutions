from seasons import convert

def test_seasons():
    assert convert('2001-01-01') == 'One million, fifty-one thousand, two hundred minutes'
    assert convert('1999-01-01') == 'Five hundred twenty-five thousand, six hundred minutes'
