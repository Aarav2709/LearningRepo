# init the vars.
p = 0
r = 0
t = 0

while p <= 0: # wait for user's input.
  p = float(input("Enter the principle: "))
  if p <= 0:
    print("Principle can't be zero. Try again!")

while r <= 0: # wait for user's input.
  r = float(input("Enter the rate: "))
  if r <= 0:
    print("Rate can't be zero. Try again!")

while t <= 0: # wait for user's input.
  t = float(input("Enter the time: "))
  if t <= 0:
    print("Time can't be zero. Try again!")

ci = p * pow((1 + r / 100), t) # calculate the compound interest.

print(f"The compound interest is {round(ci, 1)}!") # print the compound interest.
