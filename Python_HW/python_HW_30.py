import json

from datetime import datetime

INPUT_FILE = "student_courses.json"
OUTPUT_FILE = "student_courses_report.json"

def age_calculator(birth_date_str, enrollment_date_str):
    """
    The function compares the birth date with the enrollment date
    and returns the completed number of years.
    Args:
        birth_date_str (str):
            Birth date in the format "DD.MM.YYYY".
        enrollment_date_str (str):
            Enrollment date in the format "DD.MM.YYYY".
    Returns:
        int:
            Age in full years at the enrollment date.
    """
    birth_date = datetime.strptime(birth_date_str, "%d.%m.%Y")
    enrollment_date = datetime.strptime(enrollment_date_str, "%d.%m.%Y")

    age = enrollment_date.year - birth_date.year

    if (enrollment_date.month, enrollment_date.day) < (birth_date.month, birth_date.day):
        age -= 1

    return age

def main():
    """
    Generate a student enrollment report from a JSON input file.

    The function performs the following steps:
    1. Loads student data from `INPUT_FILE`.
    2. Calculates each student's age at enrollment using
       `age_calculator()`.
    3. Computes:
       - Total number of students
       - Average enrollment age
       - Number of students enrolled in each course
    4. Saves the generated report to `OUTPUT_FILE` in JSON format.
    5. Prints the report path and formatted report content.
    """
    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        students = json.load(file)

    total_students = len(students)
    total_age = 0

    students_per_course = {}

    for student in students:
        age = age_calculator(
            student["birth_date"],
            student["enrollment_date"]
        )
        total_age += age

        for course in student["courses"]:
            if course in students_per_course:
                students_per_course[course] += 1
            else:
                students_per_course[course] = 1

    average_age = round(total_age / total_students, 1) if total_students > 0 else 0

    report = {
        "total_students": total_students,
        "average_enrollment_age": average_age,
        "students_per_course": dict(sorted(students_per_course.items()))
    }

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        json.dump(report, file, ensure_ascii=False, indent=4)

    json_str = json.dumps(report, ensure_ascii=False, indent=4)

    print(f"report has been saved into: {OUTPUT_FILE}")
    print(json_str)


main()

