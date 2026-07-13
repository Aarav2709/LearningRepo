weight = float(input("Enter your weight: "))
unit = input("Enter the unit: ")

if unit == "KG":
  weight *= 2.205
  unit = "LBS"
  print(f"Your weight is {round(weight, 1)}{unit}!")
elif unit == "P":
  weight /= 2.205
  unit = "KGS"
  print(f"Your weight is {round(weight, 1)}{unit}!")
else:
  print(f"{unit} is not a valid unit.")
