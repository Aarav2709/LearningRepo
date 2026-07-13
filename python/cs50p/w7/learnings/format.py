import re # Import the library.

name = input("What's your name? ").strip() # Ask a question to the user.

if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)

print(f"Hello, {name}!")
