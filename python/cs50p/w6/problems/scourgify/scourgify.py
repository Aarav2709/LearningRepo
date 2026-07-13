import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

try:
    with open(sys.argv[1], "r") as infile:
        reader = csv.DictReader(infile)

        with open(sys.argv[2], "w", newline="") as outfile:
            writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
            writer.writeheader()

            for row in reader:
                last, first = row["name"].split(", ")
                writer.writerow({"first": first, "last": last, "house": row["house"]})

except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")
