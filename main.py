# ==========================================
# Student Management System
# Author: Prajwal Karajange
# Description:
# A simple console-based Student Management
# System built using Python.
# ==========================================

students = []


def add_student():
    """Add a new student."""
    name = input("Enter student name: ").strip().title()

    if not name:
        print("❌ Student name cannot be empty!")
        return

    if name in students:
        print("⚠️ Student already exists!")
    else:
        students.append(name)
        print("✅ Student added successfully!")


def view_students():
    """Display all students."""
    if not students:
        print("📭 No students found.")
        return

    print("\n========== STUDENT LIST ==========")

    for index, student in enumerate(sorted(students), start=1):
        print(f"{index}. {student}")

    print("----------------------------------")
    print(f"Total Students: {len(students)}")


def search_student():
    """Search a student."""
    name = input("Enter student name to search: ").strip().title()

    if name in students:
        print(f"✅ '{name}' found.")
    else:
        print(f"❌ '{name}' not found.")


def delete_student():
    """Delete a student."""
    name = input("Enter student name to delete: ").strip().title()

    if name in students:
        students.remove(name)
        print("✅ Student deleted successfully.")
    else:
        print("❌ Student not found.")


def show_menu():
    print("\n===================================")
    print("     STUDENT MANAGEMENT SYSTEM")
    print("===================================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")
    print("===================================")


def main():
    while True:
        show_menu()

        choice = input("Enter your choice: ")

        match choice:

            case "1":
                add_student()

            case "2":
                view_students()

            case "3":
                search_student()

            case "4":
                delete_student()

            case "5":
                print("\n👋 Thank you for using Student Management System!")
                break

            case _:
                print("❌ Invalid choice! Please try again.")


if __name__ == "__main__":
    main()