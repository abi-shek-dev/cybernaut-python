students = {
    "Stefin": 92,
    "Abishek": 85,
    "Karthik": 78,
    "Divya": 95,
    "Manoj": 60
}

name = "Abishek"
print(f"{name}'s grade is: {students.get(name, 'Student not found')}")

average = sum(students.values()) / len(students)
print(f"Average grade of the class: {average:.2f}")

threshold = 90
print(f"Students who scored above {threshold}:")
for student, grade in students.items():
    if grade > threshold:
        print(student)
