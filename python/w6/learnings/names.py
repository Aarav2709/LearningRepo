name = input("Enter the name: ") # Input name.

with open("names.txt", "a") as file: # File I/O, first is file name and the other value could be w [Write] or a [Append]!,
    file.write(f"{name}\n") # write() allows to input the name into file, and \n is the seperator.

with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print(f"Wassup, {line.strip()}!")


