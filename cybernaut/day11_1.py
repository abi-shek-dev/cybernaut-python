filename = "/cybernaut/student_data.txt"

num_students = int(input("Enter the number of students: "))

with open(filename, "w") as file:
    file.write("Name\t\tMarks\n")
    file.write("-" * 20 + "\n")
    for _ in range(num_students):
        name = input("Enter student name: ")
        marks = input("Enter marks: ")
        file.write(f"{name}\t\t{marks}\n")

print(f"\nData written to {filename} successfully.\n")