from calculator import square


def main():
    test_square()


def test_square():
    try:
        assert square(2) == 4  # Assert means to boldly claim something is true.
    except AssertionError:
        print("Test failed.")  # Print test failed if the condition is not met.

    try:
        assert square(3) == 9
    except AssertionError:
        print("Test failed.")  # Check calculator.py for plot twist.


if __name__ == "__main__":  # If the condition is true then execute.
    main()
