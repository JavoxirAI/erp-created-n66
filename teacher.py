import datetime

def show_my_groups():
    teacher_groups = ["Python Beginners", "Python Seniors"]
    print("Your groups:")
    for group in teacher_groups:
        print(f"- {group}")

def show_group():
    print("Group: Python Beginners")
    students = ["Ali", "Laylo", "Karim"]
    print("Students:")
    for student in students:
        print(f"- {student}")

def start_lesson():
    now = datetime.datetime.now()
    print(f"Lesson started at {now.strftime('%Y-%m-%d %H:%M:%S')}")

def homework_crud():
    print("""
Homework CRUD Menu:
1. View homeworks
2. Add homework
3. Edit homework
4. Delete homework
""")
    choice = input("Enter your choice: ")

    if choice == "1":
        view_homeworks()
    elif choice == "2":
        add_homework()
    elif choice == "3":
        edit_homework()
    elif choice == "4":
        delete_homework()
    else:
        print("Invalid choice.")

def view_homeworks():
    try:
        with open("homeworks.txt", "r") as f:
            lines = f.readlines()
            if not lines:
                print("No homework found.")
            for line in lines:
                print(line.strip())
    except FileNotFoundError:
        print("No homework file found.")

def add_homework():
    title = input("Enter homework title: ")
    description = input("Enter description: ")
    with open("homeworks.txt", "a") as f:
        f.write(f"{title}: {description}\n")
    print("Homework added.")

def edit_homework():
    title = input("Enter homework title to edit: ")
    new_description = input("Enter new description: ")
    updated = False
    try:
        with open("homeworks.txt", "r") as f:
            lines = f.readlines()
        with open("homeworks.txt", "w") as f:
            for line in lines:
                if line.startswith(title + ":"):
                    f.write(f"{title}: {new_description}\n")
                    updated = True
                else:
                    f.write(line)
        if updated:
            print("Homework updated.")
        else:
            print("Homework not found.")
    except FileNotFoundError:
        print("Homework file not found.")

def delete_homework():
    title = input("Enter homework title to delete: ")
    deleted = False
    try:
        with open("homeworks.txt", "r") as f:
            lines = f.readlines()
        with open("homeworks.txt", "w") as f:
            for line in lines:
                if not line.startswith(title + ":"):
                    f.write(line)
                else:
                    deleted = True
        if deleted:
            print("Homework deleted.")
        else:
            print("Homework not found.")
    except FileNotFoundError:
        print("Homework file not found.")
