import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$", ip):
        parts = ip.split(".")
        for part in parts:
            if part != str(int(part)) or int(part) < 0 or int(part) > 255:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()
