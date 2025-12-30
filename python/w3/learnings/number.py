def main():
    x = get_int()  # Defining X's value later.
    print(f"The integer is {x}.")  # Calling main in last.


def get_int():
    while True:  # Looping till the user actually puts an integer.
        try:  # Used to prompt python to try a program.
            return int(input("Enter an Integer: "))
        except ValueError:  # Error that is known to the developer, a subtle message is provided, instead of a context error.
            print("X is not an integer.")


main()
