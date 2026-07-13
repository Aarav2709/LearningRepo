def main():
    hello("World.")  # Define name.
    goodbye("World.")  # x2!


def hello(name):
    print(f"Hello, {name}.")  # Calling world again.


def goodbye(name):
    print(f"Goodbye, {name}.")  # :D!


if __name__ == "__main__":  # Only print name if condition is satisfied.
    main()
