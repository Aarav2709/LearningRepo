import sys
import requests

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    try:
        response = requests.get(
            "https://rest.coincap.io/v3/assets/bitcoin",
            params={"apiKey": "423f86d0fb7bc135b7e81a21d65332f90fdf019b55e40eba44a39738fab66052"}
        )
        response.raise_for_status()
        data = response.json()
        price = float(data["data"]["priceUsd"])
    except requests.RequestException:
        sys.exit("Error fetching Bitcoin price")

    cost = bitcoins * price
    print(f"${cost:,.4f}")


if __name__ == "__main__":
    main()

