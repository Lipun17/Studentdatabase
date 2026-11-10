
import json

FILE_NAME = "students.json"

rows = ["Name", "USN", "Dept", "Sub1_marks", "Sub2_marks", "Sub3_marks"]


# Load existing student records
def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


# Save student records
def save_students():
    with open(FILE_NAME, "w") as file:
        json.dump(student, file, indent=4)


# Load data when program starts
student = load_students()


# Add student
def add_student():
    data = []

    for i in rows:
        val = input(f"Enter student {i}: ").upper()
        data.append(val)

    student.append(data)

    save_students()

    print("Student added successfully...")


# Display students
def display():
    if len(student) == 0:
        print("Database is empty...")
    else:
        print("\n---------- STUDENT DATABASE ----------")

        print(f"{'Name':<15} {'USN':<15} {'Dept':<10} {'Sub1':<8} {'Sub2':<8} {'Sub3':<8}")

        for i in student:
            print(f"{i[0]:<15} {i[1]:<15} {i[2]:<10} {i[3]:<8} {i[4]:<8} {i[5]:<8}")


# Delete student
def delete_student():
    usn = input("Enter the student USN to delete: ").upper()

    for i in range(len(student)):
        if student[i][1] == usn:

            print(f"Student {student[i][0]} deleted successfully")

            student.pop(i)

            save_students()
            return

    print("Student not found...")


# Update student
def update():
    usn = input("Enter the student USN to update: ").upper()

    for i in range(len(student)):
        if student[i][1] == usn:

            data = []

            for j in rows:
                val = input(f"Enter the student {j} to update: ").upper()
                data.append(val)

            student[i] = data

            save_students()

            print("Updated successfully...")
            return

    print("Student not found...")


# Main program
print("\n       STUDENT DATABASE       ")

while True:

    print("\nSELECT FROM BELOW OPTIONS")
    print("1. Insert")
    print("2. Display")
    print("3. Delete")
    print("4. Update")
    print("5. Exit")

    try:
        op = int(input("\nEnter your choice: "))

        if op == 1:
            add_student()

        elif op == 2:
            display()

        elif op == 3:
            delete_student()

        elif op == 4:
            update()

        elif op == 5:
            print("Thank you for using Student Database!")
            break

        else:
            print("Invalid option. Try again.")

    except ValueError:
        print("Please enter a valid number.")
