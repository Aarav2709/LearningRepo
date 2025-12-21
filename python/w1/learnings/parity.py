# Taking number as a string, and defining base logic!
def main():
    num = int(input("Enter a Number: "))
    if even(num):
        print("The number is even!")
    else:
        print("The number is odd!")


# The main logic!
def even(num):
    return True if num % 2 == 0 else False


main()
