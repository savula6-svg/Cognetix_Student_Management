import csv
import os

FILE = "students.csv"

# Ensure file exists
if not os.path.exists(FILE):
    with open(FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name", "course", "email"])


def load_students():
    with open(FILE, "r") as f:
        return list(csv.DictReader(f))


def save_students(students):
    with open(FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "name", "course", "email"])
        writer.writeheader()
        writer.writerows(students)


def add_student():
    students = load_students()
    
    sid = input("Enter ID: ")
    
    if not sid.isdigit():
        print("ID must be numeric!")
        return

    for s in students:
        if s["id"] == sid:
            print("ID already exists!")
            return

    name = input("Enter Name: ")
    course = input("Enter Course: ")
    email = input("Enter Email: ")

    if "@" not in email:
        print("Invalid email!")
        return

    students.append({
        "id": sid,
        "name": name,
        "course": course,
        "email": email
    })

    save_students(students)
    print("Student added successfully!")


def view_students():
    students = load_students()
    
    if not students:
        print("No students found!")
        return

    for s in students:
        print(f"{s['id']} | {s['name']} | {s['course']} | {s['email']}")


def search_student():
    sid = input("Enter ID to search: ")
    students = load_students()

    for s in students:
        if s["id"] == sid:
            print("Found:", s)
            return

    print("Student not found!")


def delete_student():
    sid = input("Enter ID to delete: ")
    students = load_students()

    new_students = [s for s in students if s["id"] != sid]

    if len(new_students) == len(students):
        print("Student not found!")
    else:
        save_students(new_students)
        print("Student deleted!")


while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        break
    else:
        print("Invalid choice!")