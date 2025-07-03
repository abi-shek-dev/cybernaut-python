
try:
    with open("cybernaut/student_data.txt", "r") as file:
        print("Reading data from student_data.txt:\n")
        print(file.read())
except FileNotFoundError:
    print("Error: File 'student_data.txt' does not exist.")
