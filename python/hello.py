# Inputting the Name as a String.
def main():
    name = (
        input("Enter your name: ").strip().title()
    )  # Strip is used to remove extra whitespaces and Title for Capitalization.
    print(f"Hi there, {name}!")  # f is used to use variable in a string itself.


# Outputting the Name!
main()
