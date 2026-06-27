
students = []

def add_student():
    name = input("Enter name: ")
    roll = input("Enter roll no: ")

    student = {"name": name, "roll": roll}
    students.append(student)

    print("Student added successfully!")

def show_students():
    if len(students) == 0:
        print("No students found")
    else:
        for s in students:
            print("Name:", s["name"], "| Roll:", s["roll"])

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        show_students()
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice")

        