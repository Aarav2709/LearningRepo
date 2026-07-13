ans = input("Enter the answer to Great Question of Life: ").strip().lower()

match ans:
    case "forty-two" | "42" | "forty two":
        print("Yes")
    case _:
        print("No")
