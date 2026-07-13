n1 = float(input("Enter a number: "))
op = input("Enter an operator: ")
n2 = float(input("Enter another number: "))

if op == "+":
  print(f"The result is {n1+n2}!")
elif op == "-":
  print(f"The result is {n1-n2}!")
elif op == "*":
  print(f"The result is {n1*n2}!")
elif op == "/":
  print(f"The result is {n1/n2}!")
else:
  print(f"{op} is invalid operator!")
