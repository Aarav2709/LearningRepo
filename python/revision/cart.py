items = []
prices = []
total = 0

while True:
  food = input("Enter an item to buy (q to quit): ")
  if food.lower() == "q":
    break
  else:
    price = float(input("Enter the price of the item: "))
    items.append(food)
    prices.append(price)

print("Your shopping cart is: ")

for item in items:
  print(item, end = " ")

for price in prices:
  total += price

print()
print(f"Your total is ${total}!")
