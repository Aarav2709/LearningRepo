item = input("Enter the item you want to purchase: ")
price = float(input("Enter the price of the item: "))
quantity =  int(input("Enter the quantity of the item: "))

total = price*quantity

print(f"You bought {quantity} of {item}, totalling to {total}$!")
