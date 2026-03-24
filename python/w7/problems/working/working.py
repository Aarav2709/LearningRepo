import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.fullmatch(
        r'(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)',
        s
    )
    if not match:
        raise ValueError

    h1, m1, p1, h2, m2, p2 = match.groups()

    time1 = to_24(h1, m1, p1)
    time2 = to_24(h2, m2, p2)

    return f"{time1} to {time2}"


def to_24(hour, minute, period):
    hour = int(hour)
    minute = int(minute) if minute else 0

    if hour < 1 or hour > 12 or minute < 0 or minute > 59:
        raise ValueError

    if period == "AM":
        if hour == 12:
            hour = 0
    else:  # PM
        if hour != 12:
            hour += 12

    return f"{hour:02}:{minute:02}"


if __name__ == "__main__":
    main()
