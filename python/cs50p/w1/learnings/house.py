# Get the person's name.
name = input("Enter your name: ")

# Using match, an alternative for if-else.
match name:
    case (
        "Aarav" | "Arth" | "Samarth"
    ):  # | is used for multiple entries but single output.
        print("Mangal Apartment.")
    case "Aditya":
        print("Pawittra Apartments.")
    case "Pranjal":
        print("Somewhere in Noida.")
    case _:  # _ is used for the strings which are not available. Acts as else.
        print("Name not defined in database.")
