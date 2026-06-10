def calculate_average(marks):
    if not marks:
        raise ValueError("Marks list cannot be empty")

    return sum(marks) / len(marks)


def assign_grade(average):
    if average >= 90:
        return "A"
    if average >= 75:
        return "B"
    if average >= 60:
        return "C"
    if average >= 40:
        return "D"
    return "F"


def get_result(marks):
    average = calculate_average(marks)
    grade = assign_grade(average)

    return {
        "average": average,
        "grade": grade
    }


def read_marks_from_user():  # pragma: no cover
    marks_input = input("Enter marks separated by commas: ")
    return [float(mark.strip()) for mark in marks_input.split(",")]


if __name__ == "__main__":  # pragma: no cover
    student_marks = read_marks_from_user()
    result = get_result(student_marks)

    print("Student Grade Calculator")
    print(f"Average Marks: {result['average']}")
    print(f"Grade: {result['grade']}")
