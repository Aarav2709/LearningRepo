from datetime import date
import sys
import inflect

p = inflect.engine()


def main():
    dob = input("Date of Birth: ").strip()
    minutes = get_minutes(dob)
    print(convert_to_words(minutes))


def get_minutes(dob):
    try:
        year, month, day = dob.split("-")
        birth = date(int(year), int(month), int(day))
    except:
        sys.exit("Invalid date")

    today = date.today()
    delta = today - birth

    return delta.days * 24 * 60


def convert_to_words(minutes):
    words = p.number_to_words(minutes, andword="")
    return words.capitalize() + " minutes"


if __name__ == "__main__":
    main()
