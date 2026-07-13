from um import count


def test_single_um():
    assert count("um") == 1


def test_case_insensitive():
    assert count("Um") == 1
    assert count("UM") == 1


def test_with_punctuation():
    assert count("um?") == 1
    assert count("Um, thanks, um...") == 2


def test_not_substring():
    assert count("yummy") == 0
    assert count("album") == 0


def test_multiple_words():
    assert count("um um um") == 3
