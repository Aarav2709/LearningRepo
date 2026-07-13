months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ").strip()

        if "/" in date:
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
            year = int(year)

        elif "," in date:
            month_day, year = date.split(",")
            month, day = month_day.split()

            if month not in months:
                continue

            month = months.index(month) + 1
            day = int(day)
            year = int(year.strip())

        else:
            continue

        if not (1 <= month <= 12 and 1 <= day <= 31):
            continue

        print(f"{year:04}-{month:02}-{day:02}")
        break

    except ValueError:
        continue
