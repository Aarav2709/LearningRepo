from seasons import get_minutes, convert_to_words
from datetime import date


def test_minutes():
    today = date.today()
    dob = f"{today.year - 1}-{today.month:02}-{today.day:02}"
    assert get_minutes(dob) in [525600, 527040]


def test_words():
    assert convert_to_words(525600) == "Five hundred twenty-five thousand, six hundred minutes"


def test_invalid():
    try:
        get_minutes("invalid-date")
        assert False
    except SystemExit:
        assert True
