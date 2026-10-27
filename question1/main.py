# ===== Student Marks Management System =====

# Student data stored in dictionary format
student_details = [
    {"Student ID": 101, "Name": "Rahul", "Python Marks": 85, "SQL Marks": 78, "AI Marks": 90},
    {"Student ID": 102, "Name": "Anjali", "Python Marks": 72, "SQL Marks": 88, "AI Marks": 65},
    {"Student ID": 103, "Name": "Priya", "Python Marks": 70, "SQL Marks": 90, "AI Marks": 80},
]

subjects = ["Python Marks", "SQL Marks", "AI Marks"]


def get_grade(average):
    """Return a grade based on the average marks."""
    if average >= 80:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 40:
        return "C"
    else:
        return "D"


def calculate_result(student):
    """Calculate total, average, grade and pass/fail for one student."""
    marks = [student[subject] for subject in subjects]

    total = sum(marks)
    average = total / len(marks)

    student["Total"] = total
    student["Average"] = round(average, 2)
    student["Grade"] = get_grade(average)
    student["Result"] = "PASS" if average >= 40 else "FAIL"

    return student


def load_students():
    """Return the students from the dictionary list, with results calculated."""
    return [calculate_result(student) for student in student_details]


def display_students(students):
    """Print the result of every student."""
    print("\n===== Student Result =====\n")

    for s in students:
        print(f"Student ID: {s['Student ID']}")
        print(f"Name: {s['Name']}")
        print(f"Total: {s['Total']}")
        print(f"Average: {s['Average']}")
        print(f"Grade: {s['Grade']}")
        print(f"Result: {s['Result']}")
        print()


def find_highest_scorer(students):
    """Return the name of the student with the highest average."""
    best = students[0]

    for s in students:
        if s["Average"] > best["Average"]:
            best = s

    return best["Name"]


def students_above_75(students):
    """Return names of students with average above 75 (list comprehension)."""
    return [s["Name"] for s in students if s["Average"] > 75]


def main():
    students = load_students()
    display_students(students)

    print(f"Highest Scoring Student: {find_highest_scorer(students)}")

    high_scorers = students_above_75(students)
    if high_scorers:
        print("Students above 75: " + ", ".join(high_scorers))
    else:
        print("Students above 75: None")


main()