import sys  # Take the name from the command itself.

if len(sys.argv) < 2:
    print("Too few arguments.")
elif len(sys.argv) > 2:
    print("Too many arguments!")
else:
    print(f"Hello, my name is {sys.argv[1]}.")  # Store name as dictionary.
