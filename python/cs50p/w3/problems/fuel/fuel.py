while True:
    try:
        fuel = input("Enter the amount of fuel: ")
        x, y = fuel.split("/")
        x = int(x)
        y = int(y)

        if x < 0 or y < 0 or x > y:
            continue

        perc = round((x/y)*100)

        if perc <= 1:
            print("E")
        elif perc >= 99:
            print("F")
        else:
            print(f"{perc}%")

        break

    except ValueError:
        continue


