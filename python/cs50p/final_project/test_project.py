from project import calculate_percentage, assign_grade, validate_marks

def test_calculate_percentage():
    marks = {"math": 80, "science": 90}
    assert calculate_percentage(marks) == 85

def test_assign_grade():
    assert assign_grade(95) == "a"
    assert assign_grade(80) == "b"
    assert assign_grade(65) == "c"
    assert assign_grade(55) == "d"
    assert assign_grade(40) == "f"

def test_validate_marks():
    assert validate_marks("50") is True
    assert validate_marks("0") is True
    assert validate_marks("100") is True
    assert validate_marks("-1") is False
    assert validate_marks("abc") is False
