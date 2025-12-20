# Enter your marks!
marks = int(input("Enter your marks: "))
total = int(input("Enter the total marks: "))

# Begin a very LONG loop.
if marks / total >= 0.9:
    print(
        f"Your percentage is {round(marks / total * 100)} and your grade is A1! Very good!"
    )
elif marks / total >= 0.8:
    print(
        f"Your percentage is {round(marks / total * 100)} and your grade is A2! Good!"
    )
elif marks / total >= 0.7:
    print(
        f"Your percentage is {round(marks / total * 100)} and your grade is B1! Keep it up!"
    )
elif marks / total >= 0.6:
    print(
        f"Your percentage is {round(marks / total * 100)} and your grade is C1! You can definitely improve!"
    )
elif marks / total >= 0.5:
    print(
        f"Your percentage is {round(marks / total * 100)} and your grade is C2! It's fine man, you gotta work hard."
    )
elif marks / total >= 0.4:
    print(
        f"Your percentage is {round(marks / total * 100)} and your grade is D1! Okay, you have to be serious now."
    )
elif marks / total >= 0.3:
    print(
        f"Your percentage is {round(marks / total * 100)} and your grade is D2! Dude, you are on the verge to fail."
    )
else:
    print(
        f"Your percentage is {round(marks / total * 100)} and you're a failure. Give up."
    )
