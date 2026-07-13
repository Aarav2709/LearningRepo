def main():
    text = input("Input: ")
    print(shorten(text))

def shorten(w):
    vowels = "aeiouAEIOU"
    result = ""

    for c in w:
        if c not in vowels:
            result += c

    return result

if __name__ == "__main__":
    main()
