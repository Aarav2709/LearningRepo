from hello import hello  # Using pytest [pytest hello.py]!


def test_default():
    assert (
        hello() == "Hello Aarav!"
    )  # Asserting nothing, testing default values, Aarav in hello.py.


def test_args():
    assert hello("World") == "Hello World!"  # Assert arg, test that.
