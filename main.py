from auth import auth_menu, create_user_csv

def superadmin_menu():
    print("""
    Super Admin Menu:
    1. Show all admins
    2. Create admin
    3. Delete admin
    4. Show statistics
    5. Show branches
    6. Create branch
    7. Delete branch
    8. Logout
    """)
    choice = input("Enter your choice: ")
    if choice == "8":
        auth_menu()
    else:
        print("Invalide choice")
        superadmin_menu()


def admin_menu():
    print("""
    Admin Menu:
    1. Students CRUD
    2. Groups CRUD
    3. Student to group
    4. Search student
    5. Add to balance
    6. Teacher CRUD
    7. Teacher to group
    8. Logout
    """)
    choice = input("Enter your choice: ")
    if choice == "8":
        auth_menu()
    else:
        print("Invalide choice")
        admin_menu()


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
    if choice == "5":
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
    if choice == "6":
        auth_menu()
    else:
        print("Invalide choice")
        students_menu()


if __name__ == "__main__":
    create_user_csv()
    role = auth_menu()
    if role == "super_admin":
        superadmin_menu()
    elif role == "admin":
        admin_menu()
    elif role == "teacher":
        teacher_menu()
    elif role == "student":
        students_menu()
