from working import convert
import pytest

def test_function():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("5:00 PM to 9:00 AM") == "17:00 to 09:00"

def test_error_check():
    with pytest.raises(ValueError):
        convert("90AM to 5PM")
    with pytest.raises(ValueError):
        convert("9AM - 5PM")
    with pytest.raises(ValueError):
        convert("8:60 AM to 4:60 PM")


