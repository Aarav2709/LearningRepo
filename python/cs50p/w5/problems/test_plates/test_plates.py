from plates import is_valid


def test_length():
    assert is_valid("CS") is True
    assert is_valid("ABCDEFG") is False


def test_first_two_letters_required():
    assert is_valid("12AB") is False
    assert is_valid("1A234") is False
    assert is_valid("A234") is False


def test_numbers_at_end():
    assert is_valid("CS50") is True
    assert is_valid("CS5A") is False


def test_leading_zero():
    assert is_valid("CS05") is False


def test_non_alphanumeric():
    assert is_valid("CS-50") is False


def test_valid_plates():
    assert is_valid("HELLO") is True
    assert is_valid("AAA222") is True
