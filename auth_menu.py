from file_manager import read, write
from utils import hash_password

admin_phone = "admin"
admin_password = "admin"


def login():
    phone_number = input("Enter your phone number: ")
    password = input("Enter your password: ")

    if phone_number == admin_phone and password == admin_password:
        print("Welcome!")
        return "admin"

    hashed_password = hash_password(password=password)

    users = read(filename="users.csv")
    for index, user in enumerate(users):

        if user[2] == phone_number and user[3] == hashed_password:
            users[index][-1] = 1
            write(filename="users.csv", data=users)
            print(f"Welcome, {user[1]}")
            return "user"
    print("Wrong phone number or password")
    return False


def logout():
    users = read(filename="users.csv")
    for index in range(len(users)):
        users[index][-1] = 0
    write(filename="users.csv", data=users)


def get_active_user():
    users = read(filename="users.csv")
    for user in users:
        if user[-1] == "1":
            return user