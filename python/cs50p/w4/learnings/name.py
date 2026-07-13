import sys  # Take the name from the command itself.

if len(sys.argv) < 2:
    sys.exit(
        "Too few arguments."
    )  # sys.exit() is used if the condition is not matched, the program will exit with the print.
elif len(sys.argv) > 2:
    sys.exit("Too many arguments!")  # Same.
else:
    print(f"Hello, my name is {sys.argv[1]}.")  # Store name as dictionary.
