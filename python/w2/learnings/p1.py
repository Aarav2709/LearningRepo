# Question - Print a 2D Square with N Units of Length and Breadth using All Applicable Logics learnt so far.
n = int(input("Enter the Grid: "))  # Input Grid.


# Define logic.
def main():
    print_square(n)


# Main logic.
def print_square(n):
    for i in range(n):
        print("#" * n)


main()
