def main():
    greeting = input("Greeting: ")
    print(value(greeting))

def value(greeting):
    greeting = greeting.lower()

    if greeting.startstwith("hello"):
        return 0

    if greeting.startswith("h"):
        return 20

    else:
        return 100

if __name__ == "__main__":
    main()
