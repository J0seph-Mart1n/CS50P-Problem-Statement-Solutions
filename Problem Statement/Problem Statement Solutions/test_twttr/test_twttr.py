from twttr import shorten


def test_assert():
    assert shorten("hello, joseph") == "hll, jsph"
    assert shorten("HELLO, JOSEPH") == "HLL, JSPH"
    assert shorten("h3ll0, j0seph") == "h3ll0, j0sph"
    assert shorten("h@llo, j*$eph!!!") == "h@ll, j*$ph!!!"
