import pytest
from fuel import convert, gauge


def test_convert_valid():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/3") == 33


def test_convert_invalid_value():
    with pytest.raises(ValueError):
        convert("3/2")
    with pytest.raises(ValueError):
        convert("cat/dog")


def test_convert_negative():
    with pytest.raises(ValueError):
        convert("-1/2")
    with pytest.raises(ValueError):
        convert("1/-2")
    with pytest.raises(ValueError):
        convert("-1/-2")


def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_gauge_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"


def test_gauge_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"


def test_gauge_middle():
    assert gauge(50) == "50%"
