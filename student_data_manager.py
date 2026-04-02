# Student Data Manager

students = {
    "Student1": 85,
    "Student2": 78,
    "Student3": 92,
    "Student4": 74,
    "Student5": 88
}

# Print all student marks
print("Student Marks:")
for name, marks in students.items():
    print(name, ":", marks)

# Find topper
topper = max(students, key=students.get)
print("\nTopper:", topper, "-", students[topper])

# Calculate class average
average = sum(students.values()) / len(students)
print("Class Average:", average)

# Assign grades
print("\nGrades:")
for name, marks in students.items():
    if marks >= 90:
        grade = "A"
    elif marks >= 80:
        grade = "B"
    elif marks >= 70:
        grade = "C"
    else:
        grade = "D"

    print(name, "Grade:", grade)