from bank import value


def test_hello_exact():
    assert value("hello") == 0


def test_hello_with_text():
    assert value("hello there") == 0


def test_h_but_not_hello():
    assert value("hi") == 20


def test_non_h_greeting():
    assert value("good morning") == 100


def test_case_insensitive():
    assert value("HeLLo") == 0
