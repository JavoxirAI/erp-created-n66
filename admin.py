from auth import auth_menu
from file_manager import read, write
from datetime import datetime


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
    if choice == "1":
        student_crud()
    elif choice == "2":
        group_crud()
    elif choice == "3":
        student_to_group()
    elif choice == "4":
        search_student()
    elif choice == "5":
        add_to_balance()
    elif choice == "6":
        teacher_crud()
    elif choice == "7":
        teacher_to_group()
    elif choice == "8":
        auth_menu()
    else:
        print("Invalide choice")
        admin_menu()



def student_crud():
    print("""
    Student CRUD:
    1. Create student
    2. Update student
    3. Delete student
    4. Back
    """)
    choice = input("Enter your choice: ")

    users = read("user.csv")

    if choice == "1":
        username = input("Student username: ")
        password = input("Parol: ")
        created_at = datetime.now().strftime("%Y-%m-%d")
        last_id = int(users[-1][0]) if len(users) > 1 else 0
        new_student = [str(last_id + 1), username, password, "student", created_at]
        write("user.csv", new_student, mode="a")
        print("Student muvaffaqiyatli yaratildi")

    elif choice == "2":
        student_id = input("Yangilamoqchi bo‘lgan student ID sini kiriting: ")
        updated = False
        for i in range(1, len(users)):
            if users[i][0] == student_id and users[i][3] == "student":
                new_username = input("Yangi username: ")
                new_password = input("Yangi password: ")
                users[i][1] = new_username
                users[i][2] = new_password
                updated = True
                break
        if updated:
            write("user.csv", users, mode="w")
            print("Student ma'lumotlari yangilandi.")
        else:
            print("Student topilmadi.")

    elif choice == "3":
        student_id = input("O‘chirmoqchi bo‘lgan student ID sini kiriting: ")
        new_users = [users[0]]
        deleted = False
        for row in users[1:]:
            if row[0] == student_id and row[3] == "student":
                deleted = True
                continue
            new_users.append(row)
        if deleted:
            write("user.csv", new_users, mode="w")
            print("Student o‘chirildi.")
        else:
            print("Bunday student topilmadi.")

    elif choice == "4":
        admin_menu()

    else:
        print("Noto‘g‘ri tanlov.")

    student_crud()



def group_crud():
    print("""
    Groups CRUD:
    1. Create group
    2. Update group
    3. Delete group
    4. Back
    """)
    choice = input("Enter your choice: ")

    groups = read("groups.csv")

    if choice == "1":
        name = input("Guruh nomi: ")
        start_date = input("Boshlanish sanasi (yyyy-mm-dd): ")
        total_hours = input("Darslar soni (soatda): ")

        last_id = int(groups[-1][0]) if len(groups) > 1 else 0
        new_group = [str(last_id + 1), name, start_date, total_hours]
        write("groups.csv", new_group, mode="a")
        print("Guruh muvaffaqiyatli yaratildi.")

    elif choice == "2":
        group_id = input("Yangilamoqchi bo‘lgan guruh ID sini kiriting: ")
        updated = False
        for i in range(1, len(groups)):
            if groups[i][0] == group_id:
                new_name = input("Yangi nom: ")
                new_start_date = input("Yangi boshlanish sanasi (yyyy-mm-dd): ")
                new_hours = input("Yangi dars soatlari: ")
                groups[i][1] = new_name
                groups[i][2] = new_start_date
                groups[i][3] = new_hours
                updated = True
                break
        if updated:
            write("groups.csv", groups, mode="w")
            print("Guruh yangilandi.")
        else:
            print("Guruh topilmadi.")

    elif choice == "3":
        group_id = input("O‘chirmoqchi bo‘lgan guruh ID sini kiriting: ")
        new_groups = [groups[0]]
        deleted = False
        for group in groups[1:]:
            if group[0] == group_id:
                deleted = True
                continue
            new_groups.append(group)
        if deleted:
            write("groups.csv", new_groups, mode="w")
            print("Guruh o‘chirildi.")
        else:
            print("Guruh topilmadi.")

    elif choice == "4":
        admin_menu()
    else:
        print("Noto‘g‘ri tanlov.")

    group_crud()



def student_to_group():
    students = read("user.csv")
    groups = read("groups.csv")
    student_groups = read("student_groups.csv")

    print("Studentlar:")
    for student in students[1:]:
        student_id, username, _, role, _ = student
        if role == "student":
            print(f"ID: {student_id}, Username: {username}")

    print("Guruhlar:")
    for group in groups[1:]:
        group_id, group_name, _, _ = group
        print(f"ID: {group_id}, Guruh nomi: {group_name}")

    student_id_input = input("Student ID kiriting: ")
    group_id_input = input("Guruh ID kiriting: ")

    student_topildi = False
    for student in students[1:]:
        student_id, _, _, role, _ = student
        if student_id == student_id_input and role == "student":
            student_topildi = True
            break

    group_topildi = False
    for group in groups[1:]:
        group_id, _, _, _ = group
        if group_id == group_id_input:
            group_topildi = True
            break

    if not student_topildi:
        print("Bunday student yo'q")

    if not group_topildi:
        print("Bunday guruh yo'q")

    if len(student_groups) > 1:
        oxirgi_id = int(student_groups[-1][0])
    else:
        oxirgi_id = 0

    yangi_qator = [str(oxirgi_id + 1), student_id_input, group_id_input]
    write("student_groups.csv", yangi_qator, mode="a")

    print("Student guruhga biriktirildi")

    admin_menu()



def search_student():
    students = read("user.csv")
    groups = read("groups.csv")
    student_groups = read("student_groups.csv")

    student_id_input = input("Qidirilayotgan student ID sini kiriting: ")

    student_found = False
    for student in students[1:]:
        student_id, username, _, role, _ = student
        if student_id == student_id_input and role == "student":
            print(f"Student: ID={student_id}, Username={username}")
            student_found = True
            break

    if not student_found:
        print("Bunday student topilmadi")

    group_ids = []
    for row in student_groups[1:]:
        link_id, s_id, g_id = row
        if s_id == student_id_input:
            group_ids.append(g_id)

    if not group_ids:
        print("Bu student hech qanday guruhga biriktirilmagan.")

    print("Student quyidagi guruhlarda o‘qiydi:")
    for group in groups[1:]:
        group_id, group_name, start_date, total_hours = group
        if group_id in group_ids:
            print(f"- ID: {group_id}, Nomi: {group_name}, Boshlanish: {start_date}, Soatlar: {total_hours}")

    admin_menu()




def add_to_balance():
    students = read("user.csv")
    balances = read("balance.csv")

    student_id_input = input("Student ID ni kiriting: ")

    student_exists = False
    for student in students[1:]:
        student_id, username, _, role, _ = student
        if student_id == student_id_input and role == "student":
            student_exists = True
            print(f"Student: {username} (ID: {student_id})")
            break

    if not student_exists:
        print("Bunday student mavjud emas.")

    try:
        add_amount = float(input("Qo‘shiladigan summa: "))
    except ValueError:
        print("Noto‘g‘ri raqam.")
        return

    updated = False
    for row in balances[1:]:
        if row[1] == student_id_input:
            current_balance = float(row[2])
            row[2] = str(current_balance + add_amount)
            updated = True
            break

    if not updated:
        new_id = str(int(balances[-1][0]) + 1 if len(balances) > 1 else 1)
        new_row = [new_id, student_id_input, str(add_amount)]
        write("balance.csv", new_row, mode="a")
    else:
        write("balance.csv", balances, mode="w")

    print("Balans muvaffaqiyatli yangilandi.")

    admin_menu()



def create_teacher():
    users = read("user.csv")
    username = input("Teacher username: ")
    password = input("Parol: ")
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_id = str(int(users[-1][0]) + 1 if len(users) > 1 else 1)
    teacher_row = [new_id, username, password, "teacher", now]
    write("user.csv", teacher_row, mode="a")
    print(f"Teacher '{username}' muvaffaqiyatli qo‘shildi.")

def update_teacher():
    users = read("user.csv")
    teacher_id = input("O‘zgartiriladigan teacher ID: ")
    updated = False

    for user in users:
        if user[0] == teacher_id and user[3] == "teacher":
            user[1] = input("Yangi username: ")
            user[2] = input("Yangi parol: ")
            updated = True
            break

    if updated:
        write("user.csv", users, mode="w")
        print(f"Teacher ID {teacher_id} yangilandi.")
    else:
        print("Teacher topilmadi.")

def delete_teacher():
    users = read("user.csv")
    teacher_id = input("O‘chiriladigan teacher ID: ")
    new_users = [users[0]]
    deleted = False

    for user in users[1:]:
        if user[0] == teacher_id and user[3] == "teacher":
            deleted = True
        else:
            new_users.append(user)

    if deleted:
        write("user.csv", new_users, mode="w")
        print(f"Teacher ID {teacher_id} o‘chirildi")
    else:
        print("Teacher topilmadi")

def teacher_crud():
    print("""
    Teacher CRUD:
    1. Yangi teacher qo'shish
    2. Teacher ma'lumotlarini yangilash
    3. Teacher o'chirish
    4. Orqaga
    """)
    choice = input("Enter your choice: ")

    if choice == "1":
        create_teacher()
    elif choice == "2":
        update_teacher()
    elif choice == "3":
        delete_teacher()
    elif choice == "4":
        admin_menu()
    else:
        print("Invalide choice")
        teacher_crud()




def teacher_to_group():
    teachers = read("user.csv")
    groups = read("groups.csv")

    print("Mavjud o'qituvchilar:")
    for teacher in teachers[1:]:
        if teacher[3] == "teacher":
            print(f"ID: {teacher[0]}, Username: {teacher[1]}")

    teacher_id = input("O'qituvchi ID ni kiriting: ")

    print("Mavjud guruhlar:")
    for group in groups[1:]:
        print(f"ID: {group[0]}, Group Name: {group[1]}")

    group_id = input("Guruh ID ni kiriting: ")

    found_teacher = False
    found_group = False

    for teacher in teachers[1:]:
        if teacher[0] == teacher_id and teacher[3] == "teacher":
            found_teacher = True
            break

    for group in groups[1:]:
        if group[0] == group_id:
            found_group = True
            break

    if found_teacher and found_group:
        group_data = groups[1:]
        for group in group_data:
            if group[0] == group_id:
                group.append(teacher_id)
                write("groups.csv", groups, mode="w")
                print(f"O'qituvchi ID {teacher_id} muvaffaqiyatli guruhga qo'shildi")
    else:
        print("O'qituvchi yoki guruh topilmadi.")
        teacher_to_group()

    admin_menu()
