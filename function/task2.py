def grade_text(grade_number):
    if grade_number < 3:
        return "Fail"
    elif grade_number < 3.50:
        return "Poor"
    elif grade_number < 4.50:
        return "Good"
    elif grade_number < 5.50:
        return "Very Good"
    else:
        return "Excellent"

current_grade = float(input())

print(grade_text(current_grade))
