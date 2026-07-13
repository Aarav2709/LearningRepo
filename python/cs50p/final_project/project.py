def main(): # this is my project. the main function is responsible for intaking all values and providing the final output.
    subjects = get_subjects()
    marks = get_marks(subjects)
    percentage = calculate_percentage(marks)
    grade = assign_grade(percentage)
    highest, lowest = find_extremes(marks)
    advice = generate_advice(marks)

    print("percentage:", round(percentage, 2))
    print("grade:", grade)
    print("highest:", highest)
    print("lowest:", lowest)
    print("advice:", advice)

def get_subjects(): # here, the user inputs the subjects, and all the values are converted into lowercase and trailing whitespaces are also removed.
    subjects = input("enter subjects separated by comma: ").lower().split(",")
    return [s.strip() for s in subjects if s.strip()] # each value is stored as a key.

def get_marks(subjects): # here, we ask the user to input their marks.
    marks = {}
    for subject in subjects: # the subjects [keys] are accessed.
        while True:
            value = input(f"enter marks for {subject}: ").lower()
            if validate_marks(value):
                marks[subject] = int(value)
                break
            else:
                print("invalid input!")
    return marks

def calculate_percentage(marks): # the percentage is calculate by summing up all the values and dividing it.
    total = sum(marks.values())
    return total / len(marks)

def assign_grade(percentage): # the values are then passed on and the percentage is used to assign a grade to the user.
    if percentage >= 90:
        return "a"
    elif percentage >= 75:
        return "b"
    elif percentage >= 60:
        return "c"
    elif percentage >= 50:
        return "d"
    else:
        return "f"


def find_extremes(marks): # extremes are used to find consistencies using a value, "diff".
    highest = max(marks, key=marks.get)
    lowest = min(marks, key=marks.get)
    return highest, lowest


def generate_advice(marks): # advice is generated, using the "find_extremes" function.
    values = list(marks.values())
    avg = sum(values) / len(values)
    diff = max(values) - min(values)

    if diff <= 10:
        consistency = "consistent performance."
    else:
        consistency = "inconsistent performance."

    weak = min(marks, key=marks.get)
    strong = max(marks, key=marks.get)

    return f"strong in {strong}, improve in {weak}, {consistency}."

def validate_marks(value): # marks are validated and ensured its between 0 to 100.
    if value.isdigit():
        num = int(value)
        return 0 <= num <= 100
    return False

if __name__ == "__main__": # execute.
    main()
