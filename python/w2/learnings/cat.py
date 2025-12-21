# Storing number as string.
n = int(input("Enter the number of times you wanna meow: "))


# Calling the string.
def main():
    meow(n)


# Main logic.
def meow(n):
    for _ in range(n):
        print("Meow!")


main()
