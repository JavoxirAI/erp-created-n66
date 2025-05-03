from admin import admin_menu
from auth import auth_menu, create_user_csv
from super_admin import show_all_admins, create_admin, delete_admin, show_statistics
from teacher import show_my_groups, show_group, start_lesson, homework_crud
from student import show_groups, upload_homework, show_balance, show_attendance, make_payment


def main():
    print("""
    Roles:
    1. Super admin
    2. Admin
    3. Teacher
    4. Student
    """)
    choice = input("Enter your choice: ")

    if choice == "1":
        superadmin_menu()
    elif choice == "2":
        admin_menu()
    elif choice == "3":
        teacher_menu()
    elif choice == "4":
        students_menu()
    else:
        print("Invalid choice!")
    main()


def superadmin_menu():
    print("""
    Super Admin Menu:
    1. Show all admins
    2. Create admin
    3. Delete admin
    4. Show statistics
    5. Logout
    """)
    choice = input("Enter your choice: ")

    if choice == "1":
        show_all_admins()
    elif choice == "2":
        create_admin()
    elif choice == "3":
        delete_admin()
    elif choice == "4":
        show_statistics()
    elif choice == "5":
        auth_menu()
    else:
        print("Invalide choice")
    superadmin_menu()




def teacher_menu():
    print("""
    Teacher Menu:
    1. My groups
    2. Show group
    3. Start the lesson
    4. Homework CRUD
    5. Logout
    """)
    choice = input("Enter your choice: ")

    if choice == "1":
        show_my_groups()
    elif choice == "2":
        show_group()
    elif choice == "3":
        start_lesson()
    elif choice == "4":
        homework_crud()
    elif choice == "5":
        auth_menu()
    else:
        print("Invalide choice")
    teacher_menu()


def students_menu():
    print("""
    Student Menu:
    1. Show groups
    2. Upload homework
    3. Show my attendance
    4. Show my balance
    5. Payment
    6. Logout
    """)
    choice = input("Enter your choice: ")

    if choice == "1":
        show_groups()
    elif choice == "2":
        upload_homework()
    elif choice == "3":
        show_attendance()
    elif choice == "4":
        show_balance()
    elif choice == "5":
        make_payment()
    elif choice == "6":
        auth_menu()
    else:
        print("Invalide choice")
    students_menu()


if __name__ == "__main__":
    create_user_csv()
    role = main()
    # if role == "super_admin":
    #     superadmin_menu()
    # elif role == "admin":
    #     admin_menu()
    # elif role == "teacher":
    #     teacher_menu()
    # elif role == "student":
    #     students_menu()
