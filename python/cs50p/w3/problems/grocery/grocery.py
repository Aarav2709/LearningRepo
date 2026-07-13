grocery = {}

while True:
    try:
        item = input().strip().lower()
        if item:
            grocery[item] = grocery.get(item, 0) + 1
    except EOFError:
        break

for item in sorted(grocery):
    print(f"{grocery[item]} {item.upper()}")
