from file_manager import read, write

superadmin_name = "super_admin"
superadmin_pass = "super_admin"


def login():
    user_name = input("Enter your phone number: ")
    user_pass = input("Enter your password: ")

    if user_name == superadmin_name and user_pass == superadmin_pass:
        print("Welcome!")
        return "admin"


    users = read(filename="users.csv")
    for index, user in enumerate(users):

        if user[2] == user_name and user[3] == user_pass:
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
