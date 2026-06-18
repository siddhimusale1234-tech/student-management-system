students = []

while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter student name: ")

        students.append(name)

        print("Student Added Successfully!")

    elif choice == "2":

        if len(students) == 0:
            print("No Students Found.")

        else:
            print("\nStudent List:")

            for student in students:
                print(student)

    elif choice == "3":

        search_name = input("Enter student name to search: ")

        if search_name in students:
            print("Student Found!")

        else:
            print("Student Not Found!")

    elif choice == "4":

        delete_name = input("Enter student name to delete: ")

        if delete_name in students:
            students.remove(delete_name)
            print("Student Deleted Successfully!")

        else:
            print("Student Not Found!")

    elif choice == "5":

        print("Thank You!")
        break

    else:

        print("Invalid Choice! Please Try Again.")