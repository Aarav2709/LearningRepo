def main():
    name = input("Enter your name: ")
    print(hello(name))


def hello(to="Aarav"):
    return f"Hello, {to}!"


if __name__ == "__main__":
    main()
