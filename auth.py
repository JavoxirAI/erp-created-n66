from datetime import datetime
from file_manager import read
import os

superadmin_name = "super_admin"
superadmin_pass = "super_admin"

current_user = None

def create_user_csv():
    if not os.path.exists("data/user.csv"):
        users = [
            ["id", "username", "password", "rol", "creat_add"],
            ["1", "admin1", "admin123", "admin", datetime.now().isoformat()],
            ["2", "teacher1", "teach123", "teacher", datetime.now().isoformat()],
            ["3", "student1", "stud123", "student", datetime.now().isoformat()],
        ]
        from file_manager import write
        write("user.csv", users, mode="w")
        print("user.csv created.\n")


def login():
    global current_user
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == superadmin_name and password == superadmin_pass:
        print("Welcome, Super Admin!\n")
        current_user = {"username": username, "rol": "super_admin"}
        return "super_admin"

    users = read("user.csv")
    for row in users:
        id_, uname, upass, role, _ = row
        if uname == username and upass == password:
            print(f"Welcome, {role.capitalize()}!\n")
            current_user = {"id": id_, "username": uname, "rol": role}

            return role


    print("Invalid user or password")
    return None


def auth_menu():
    print("""
    Auth Menu:
    1. Login
    2. Exit
    """)
    choice = input("Enter your choice: ")
    if choice == "1":
        role = login()
        if role:
            return role
        else:
            auth_menu()
    elif choice == "2":
        print("👋 Goodbye!")
        exit()
    else:
        print("Invalid choice!")
        auth_menu()
