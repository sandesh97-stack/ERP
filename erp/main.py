1# main.py

from file_handler import load_data, save_data
import operations
import analytics


def menu():
    load_data()

    while True:
        print("\n====== ERP SYSTEM ======")
        print("1. Register Student")
        print("2. View Courses")
        print("3. Register Course")
        print("4. View Registered Courses")
        print("5. Credit Analysis")
        print("6. Department Visualization")
        print("7. Save Data")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            operations.register_student()
        elif choice == '2':
            operations.view_courses()
        elif choice == '3':
            operations.register_course()
        elif choice == '4':
            operations.view_registered_courses()
        elif choice == '5':
            analytics.credit_analysis()
        elif choice == '6':
            analytics.department_visualization()
        elif choice == '7':
            save_data()
        elif choice == '8':
            save_data()
            print("Exiting...")
            break
        else:
            print("Invalid choice")


menu()