import time

my_time = int(input("Enter the time (s) you wanna start the CD from: "))

for i in range(my_time, 0, -1):
  print(f"{i}s remaining!")
  time.sleep(1)

print("Time is up.")
